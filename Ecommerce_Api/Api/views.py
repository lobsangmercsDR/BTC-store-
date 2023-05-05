from rest_framework.views import APIView
from django.http import response
from rest_framework import viewsets,permissions, authentication,mixins, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.http.response import JsonResponse 
from .authentications import IsAdmin, IsSeller, IsChecker, IsBuyer, IsGroupAccepted, AllowAny
from rest_framework.decorators import api_view
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework.authtoken.models import  Token
from django.contrib.auth.models import Group
from django.db.models import Q
from datetime import datetime, timedelta
from .utils import services as uti
from django.core import serializers
from .models import Product,Category,Transacts,User,InvitationCodes,RoleRequests
from .serializers import (TransactsSerializer, 
                          CategorySerializer,
                          CategoryWithoutProductsSerializer, 
                          ProductSerializer,
                          UserSerializer,
                          UserCreatorSerializer,
                          UserNestedSerializer,
                          InvitationCodesSerializer,
                          RoleRequestsSerializer,
                          AuthenticationSerializer,
                          GroupsSerializer)

def format_data(data=None, nameClass=None, code=200):
    status = 0
    if data==None and nameClass==None and code==200:
        return "No hay nada en la funcion"
    if code ==500:
        return {'message':'Ha habido un error en el servidor', 'status':code}
    if (len(data) > 0):
        result = {
            'success':True,
            nameClass:data,
            'status':code
        }
    else: 
        result = {
            'success':False,
            'message': f'No hay {nameClass} en la BD',
            'status':404
        }
    return result

def hasOrNotPermission(clss, request, view,obj=None,authClass=None, oneObj=False):
    if authClass != None:
        if oneObj== False:
            userComp = True if authClass.has_permission(clss, request, view) else False

        else:
            userComp = True if authClass.has_object_permission(clss, request,view,obj) else False
    return userComp



def validate_credentials(request,userProperty=None,groups=[],is_one_item=False, is_limited=False):
    if request.user.is_authenticated ==  False:
       return {'success':False,'status':401, 'message':'No esta autorizado'}
    validator = validate_group(request.user, ['administrator','sellers', 'checkers','buyers'])
    if validator == False and request.user.is_superuser == False:
        return {'success':False,'status':403}
    if is_limited:
            return {'success':True, 'userid':request.user.id}
    if is_one_item and is_limited:
        if validate_group(request.user, groups):
            if userProperty.id != request.user.id:
                return {'success':False,'status':403}


def validate_group(user, groups):
    if list(user.groups.values_list('name',flat=True)) == []:
        return None
    if list(user.groups.values_list('name',flat=True))[0] not in groups:
        return False
    else:
        return True


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated,IsGroupAccepted]

    # GET all Products (with restrictions for sellers)
    def nested_list_products(self, request):
        user_products= request.GET.get('userProducts','false')
        last_products= request.GET.get('lately','false')
        digital=request.GET.get('digital','false')
        start_time= datetime.now()-timedelta(hours=24)
        filters = {
            'seller_id': None if user_products =='false' else request.user.id,
            'active': True if user_products == 'true' else None,
            'dateReleased__gte': start_time if last_products =='true' and not user_products == 'true' else None,
            'is_digital': True if digital == 'true' else None,
        }
        products = Product.objects.all()
        for key, value in filters.items():
            if value is not None:
                products = products.filter(Q(**{key: value}))
        if not products:
            return JsonResponse({"Message": "No se encontraron productos con los presentes requerimientos"})
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    
    # GET just one product (Also with restricctions)
    def get_product(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data,status=200)

    # POST a new product (Taking Seller id)
    def post_product(self,request):
        sellerPermision = hasOrNotPermission(self, request,self.__class__, authClass=IsSeller)
        checkerPermision = hasOrNotPermission(self, request,self.__class__, authClass=IsChecker)
        buyerPermsision = hasOrNotPermission(self, request,self.__class__, authClass=IsBuyer)
        userPerm = uti.hasOrNotPermission(self, request,self.__class__, authClass=[IsSeller,IsChecker,IsBuyer,IsAdmin])
        print(userPerm)
        print(request.data)
        if not userPerm["IsSeller"] and not userPerm["IsAdmin"]:
            return JsonResponse({"message":"No tiene permiso para realizar esta accion"}, status=403)
        serializer = ProductSerializer(data=request.data, context={'request':request, 'userPermision':userPerm})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.get_success_headers(serializer.data)
        return JsonResponse(serializer.data, status=200)
 
    # PUT a product created by a seller
    def update_product(self, request,*args, **kwargs):
        instance = self.get_object()
        userPerm = uti.hasOrNotPermission(self, request,self.__class__, authClass=[IsSeller,IsAdmin,IsChecker,IsBuyer],oneObj=True, obj=instance)
        print(userPerm)
        if not any(val is True for val in userPerm.values() if val != "IsSeller" or "IsBuyer"):  
            return JsonResponse({'success':False, 'message':'No ha vendido este producto'}, status=404)
        serializer = self.get_serializer(instance,data=request.data, partial=True, context={'userPermision':userPerm})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return JsonResponse({'message':'El campo ha sido actualizado','result':serializer.data, 'status':200}, status=200)

    # DELETE Product (with restrictions)
    def delete_product(self, request, *args, **kwargs):
        instance= self.get_object()
        userPerm = uti.hasOrNotPermission(self, request,self.__class__, authClass=[IsSeller,IsAdmin],oneObj=True, obj=instance)
        print(userPerm)
        if not any(val is True for val in userPerm.values()):
            return JsonResponse({"message":"No tiene acceso a esta funcionalidad o producto"}, status=403)
        self.perform_destroy(instance)
        return JsonResponse({"Success":True, "message":"El producto fue borrado correctamente"}, status=200)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated,IsGroupAccepted]

    @api_view(['GET'])
    #GET all Categories
    def nested_list_categories(self, request):
        incldProd = request.GET.get('prod','false')
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        if incldProd == 'true': 
            for item in serializer.data:
                item.pop('products')
        return JsonResponse(serializer.data, status=200, safe=False)   


    # GET one Category 
    def get_category(self, request, *args,**kwargs):
        incldProd = request.GET.get('prod','false')
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        result = serializer.data
        
        if incldProd == 'true': 
            result.pop('products')
            print(result)
        return JsonResponse(result, status=200)
        
    # POST One category
    def post_category(self, request):
        userPermision = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin])
        if not userPermision['IsAdmin']:
            return JsonResponse({'message':'No esta autorizado para esto'},status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return JsonResponse(serializer.data, status=200)
    
    def update_category(self, request, *args, **kwargs):
        userPermision = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin])
        if not userPermision['IsAdmin']:
            return JsonResponse({'message':'No esta autorizado para esto'},status=400)
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return JsonResponse({'message':'El campo ha sido actualizado','result':serializer.data,'status':200}, status=200)

    # DELETE Category
    def destroy_category(self, request, *args, **kwargs):
        userPermision = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin])
        if not userPermision['IsAdmin']:
            return JsonResponse({'message':'No esta autorizado para esto'},status=400)
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({'message': 'El campo fue borrado correctamente', 'status':200}, status=200)

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, IsGroupAccepted]

    def get_all_users(self, request, *args, **kwargs):
        userPermision = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin])
        if not userPermision['IsAdmin']:
            instances = User.objects.filter(id=request.user.id)
        else:
            instances = User.objects.all()
        serializer  = UserSerializer(instances, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
        
    def post_user(self, request, *args, **kwargs):
        serializer = UserCreatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        serializerRep = UserSerializer(user)   
        return JsonResponse(serializerRep.data, status=200)

    def put_user_data(self, request, *args, **kwargs):
        roles=request.GET.get('roles','false')
        userObj = self.get_object()
        print(userObj)
        userPermision = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin, IsSeller,IsChecker, IsBuyer], oneObj=True, obj=userObj)
        print(userPermision)
        if not any(val is True for val in userPermision.values()):
            return JsonResponse({"message":"No tiene acceso a este objeto",'ID':request.user.id})
        if not userPermision['IsAdmin'] and roles=='true':
            return JsonResponse({'message':'No tiene permiso para esta funcion'}, status=403)
        serializer = UserCreatorSerializer(userObj,data=request.data, partial=True, context={"roles":roles})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        serializer= UserSerializer(userObj)
        print(serializer.data)
        return JsonResponse(serializer.data, status=200)
    
    def post_groups_request(self, request):
        serializer = RoleRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()   
        return JsonResponse(serializer.data, status=200)
    


    # GET one User
    def get_user(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        result = format_data(serializer.data)
        return JsonResponse(result, status=200)


    # DELETE one User
    def delete_user(self, request, *args, **kwargs):
        instance=self.get_object()
        userPermision = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin],oneObj=True,obj=instance)
        if not userPermision['IsAdmin']:
            return {'message':'Largo de aqui'}
        self.perform_destroy(instance=instance)
        return JsonResponse({'message':'El usuario ha sido eliminado correctamente', 'status':200}, status=200)
    
    def get_permissions(self):
        if self.action == 'post_user':
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

class LogoutView(APIView):
    permission_classes = [IsAuthenticated,IsGroupAccepted]

    def get(self, request, *args, **kwargs):
        dataAuth = request.headers.get('Authorization')
        token = dataAuth.split(' ')[1]
        token1 = Token.objects.filter(key=token).first()
        print(type(token1))
        token1.delete()
        return JsonResponse({'message':'Token Borrado Exitosamente'}, status=200)
    
class AuthenticationView(ObtainAuthToken):
    serializer_class = AuthenticationSerializer

class TransactsView(viewsets.ModelViewSet):
    queryset = Transacts.objects.all()
    serializer_class = TransactsSerializer
    permission_classes = [IsAuthenticated, IsGroupAccepted]

    def get_all_transacts(self, request):
        userPermision = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin])
        if not userPermision['IsAdmin']:
            transacts = Transacts.objects.filter(buyers_id=request.user.id)
        else:
            transacts = Transacts.objects.all()
        serializer= TransactsSerializer(transacts, many=True)   
        dicc = serializer.data
        return JsonResponse(dicc, status=200, safe=False)

    def post_transact(self, request):
        serializer = TransactsSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    def delete_transact(self, request, *args, **kwargs):
        transact = self.get_object()
        userPermision = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin, IsSeller, IsBuyer], oneObj=True,obj=transact)
        print(userPermision)
        if not any(value for value in userPermision.values()):
            return JsonResponse({'message':'No tiene permiso para realizar esta accion'}, status=403)
        self.perform_destroy(transact)
        return JsonResponse({'message':'Transaccion eliminada exitosamente'},status=204)

class GroupsView(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupsSerializer

    def nested_list(self, request):
        groups = Group.objects.all()
        serializer = GroupsSerializer(groups, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, status=200, safe=False)

class InvitationCodeView(viewsets.ModelViewSet):
    queryset = InvitationCodes.objects.all()
    serializer_class = InvitationCodesSerializer
    permission_classes = [IsAuthenticated,IsAdmin]

    def get_invitation_codes(self, request):
        invCodes = InvitationCodes.objects.all()
        result = InvitationCodesSerializer(invCodes, many=True).data
        print(result)
        return JsonResponse(result, status = 200, safe=False)

    def post_invitation_code(self, request):
        invitation = InvitationCodesSerializer(data=request.data)
        if invitation.is_valid(raise_exception=True):
            values = invitation.save()
            result = InvitationCodesSerializer(values).data
            return JsonResponse(result, status=201)
        return JsonResponse({"success":False},status=400)

class RoleRequestsView(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated,IsGroupAccepted]
    serializer_class = RoleRequestsSerializer

    def get_role_requests(self, request):
        still = False if request.GET.get('still','false') == 'true' else True
        is_pass = True if request.GET.get('isPass', 'false') == 'true' else False
        userPerm = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin])
        print(userPerm)
        if not userPerm['IsAdmin']:
            return JsonResponse({'message':'No tiene permiso para realizar esta accion'})
        else:
            print(still)
            print(is_pass)
            if not still and not is_pass:
                request = RoleRequests.objects.all()
            elif is_pass:
                request = RoleRequests.objects.filter(is_password=is_pass)
            elif still:
                request = RoleRequests.objects.filter(approved=True)
            else:
                request = RoleRequests.objects.filter(approved=True, is_password=is_pass)
            serializer = RoleRequestsSerializer(request, many=True)
            return JsonResponse(serializer.data,status=200, safe=False)

    def post_role_request(self, request):
        print(request.data)
        userPerm = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin])


        if not userPerm['IsAdmin'] and 'approved' in request.data.keys(): 
            return JsonResponse({"message":"No tiene permiso para realizar esta accion"}, status=401)

        serializer = RoleRequestsSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)
