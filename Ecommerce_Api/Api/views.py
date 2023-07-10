from rest_framework.views import APIView
from django.http import response
from django.db.models import Case, When
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from rest_framework import viewsets,permissions, authentication,mixins, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.http.response import JsonResponse 
from .authentications import IsAdmin, IsSeller, IsChecker, IsBuyer, IsGroupAccepted, AllowAny
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
import requests as Rq
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework.authtoken.models import  Token
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import FileResponse
from datetime import datetime, timedelta
import os
from .utils import services as uti
from django.core import serializers
from django.http import HttpResponse
from .models import ProductFisic,MethodProducts,Withdrawals,ReportTransacts,CheckerSolic,TransactCategories,ProductDigit,Category,Transacts,User,InvitationCodes,RoleRequests, SubCategory
from .serializers import (TransactsSerializer,
                          TransactCategorySerializer,
                          ReportSerializer,
                          SolicCheckerSerializer,
                          CategorySerializer,
                          WithDrawSerializer,
                          ProductDigitSerializer,
                          CategoryWithoutProductsSerializer, 
                          ProductSerializer,
                          UserSerializer,
                          UserCreatorSerializer,
                          UserNestedSerializer,
                          InvitationCodesSerializer,
                          RoleRequestsSerializer,
                          AuthenticationSerializer,
                          GroupsSerializer,
                          MethodSerializer,
                          StoreSerializer,
                          SubCategorySerializer)

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
    

class WithDrawView(viewsets.ModelViewSet):
    queryset = Withdrawals.objects.all()
    serializer_class = WithDrawSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = []

    
    def get_withdraws(self, request):
        objects = Withdrawals.objects.filter(user=request.user.id)
        serializer = WithDrawSerializer(objects, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    def post_new_withdraw(self, request):
        data = request.data
        user = request.user
        serializer = WithDrawSerializer(data=data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=200)


class Img_view(viewsets.ModelViewSet):
    def get_file_img(self, request, image_name):
        work_route=  r'C:\Users\TI\Documents\Proyectos\Frontend\Vue\AlanStore\Ecommerce_Api\images'
        local_route= r'C:\Users\alan8\OneDrive\Documentos\Frontend\Vue\AlanStore\Ecommerce_Api\images'
        complete_path = os.path.join(local_route, image_name)
        
        if os.path.exists(complete_path):
            return FileResponse(open(complete_path,'rb'),content_type='image/jpeg')
        else:
            return JsonResponse({'error':'No se encuentra la imagen'})


class TransactSubcategoryView(viewsets.ModelViewSet):
    queryset = TransactCategories.objects.all()
    serializer_class = TransactCategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, IsGroupAccepted]
    
    def get(self, request):
        transactse= TransactCategories.objects.all()
        serializer = TransactCategorySerializer(transactse, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    def post(self, request):
       serializer = TransactCategorySerializer(data=request.data, context={'request':request})
       user = User.objects.get(id=request.user.id)
       if UserSerializer(user).data['group'] == "buyers":
            userSer = UserCreatorSerializer(user, data={'change_group':'seller'}, partial=True,context={'update':True}) 
            userSer.is_valid(raise_exception =True)
            self.perform_update(userSer)
            print("Con exito")
       serializer.is_valid(raise_exception=True)
       self.perform_create(serializer=serializer)
       return JsonResponse(serializer.data, status=200)


class ProductView(viewsets.ModelViewSet):
    queryset = ProductFisic.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [IsAuthenticated,IsGroupAccepted]
    pagination_class = Paginator

    def get_all_methods(self, request):
        query = MethodProducts.objects.all()
        paginator = Paginator(query, per_page=5)
        page_number= request.GET.get('page',1)
        if int(page_number) > paginator.num_pages:
            return JsonResponse({"error":"No hay mas paginas"}, status=404)
        paginated_data = paginator.get_page(page_number) 
        serializer= MethodSerializer(paginated_data, many=True) 
        dicc = {
            "actual_page": int(page_number),
            "available_pages":  paginator.num_pages - int(page_number),
            "data": serializer.data
        }
        return JsonResponse(dicc, status=200, safe=False)
    
    def get_method(self, request, *args, pk):
        instance = MethodProducts.objects.get(id=pk)
        print(instance)
        serializer = MethodSerializer(instance)
        result = serializer.data
        return JsonResponse(result, status=200)


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
        products = ProductFisic.objects.all()
        for key, value in filters.items():
            if value is not None:
                products = products.filter(Q(**{key: value}))
        if not products:
            return JsonResponse({"Message": "No se encontraron productos con los presentes requerimientos"})
        paginator = Paginator(products, per_page=5)
        page_number= request.GET.get('page',1)
        if int(page_number) > paginator.num_pages:
            return JsonResponse({"error":"No hay mas paginas"}, status=404)
        paginated_data = paginator.get_page(page_number) 
        serializer= ProductSerializer(paginated_data, many=True) 
        dicc = {
            "actual_page": int(page_number),
            "available_pages":  paginator.num_pages - int(page_number),
            "data": serializer.data
        }
        return JsonResponse(dicc, status=200, safe=False)

    
    # GET just one product (Also with restricctions)
    def get_product(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductSerializer(instance)
        return JsonResponse(serializer.data,status=200)
        
    def get_digit_product(self, request, *args, pk):
        try:
            instance = ProductDigit.objects.get(id=pk)
            serializer = ProductDigitSerializer(instance)
            result = serializer.data
            return JsonResponse(result, status=200)
        except: 
            return JsonResponse({"error":"no existe"}, status=200)



    # POST a new product (Taking Seller id)
    def post_product(self,request):
        userPerm = uti.hasOrNotPermission(self, request,self.__class__, authClass=[IsSeller,IsChecker,IsBuyer,IsAdmin])
        if not userPerm["IsSeller"] and not userPerm["IsAdmin"]:
            return JsonResponse({"message":"No tiene permiso para realizar esta accion"}, status=403)
        print(request.data)
        serializer = ProductSerializer(data=request.data, context={'request':request, 'userPermision':userPerm})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.get_success_headers(serializer.data)
        return JsonResponse(serializer.data, status=200)
 
    # PUT a product created by a seller
    def update_product(self, request,*args, **kwargs):
        instance = self.get_object()
        userPerm = uti.hasOrNotPermission(self, request,self, authClass=[IsSeller,IsAdmin,IsChecker,IsBuyer],oneObj=True, obj=instance)
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


class ProductsDigitView(viewsets.ModelViewSet):
    queryset = ProductDigit.objects.all()
    serializer_class = ProductDigitSerializer
    pagination_class = Paginator

    # GET all digital products
    def get_digit_products(self, request):
        digitProducts = ProductDigit.objects.all().order_by('-dateCreated')
        paginator = self.pagination_class(digitProducts, per_page=12)
        page_number= request.GET.get('page',1)
        if int(page_number) > paginator.num_pages:
            return JsonResponse({"error":"No hay mas paginas"}, status=404)
        paginated_data = paginator.get_page(page_number)
        print(paginated_data[0],222222)
        serializer = ProductDigitSerializer(paginated_data,context={'request':request}, many=True)
        return JsonResponse({'available_pages':paginator.num_pages-int(page_number),'page':int(page_number),'data':serializer.data}, status=200, safe=False)

    def post_product_digit(self, request):
        data = request.data
        serializer = ProductDigitSerializer(data=data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    
    def put_Product_state(self, request,pkS,pk):
        try:
            product = ProductDigit.objects.get(id=pk)
            solic = CheckerSolic.objects.get(id=pkS)
        except Exception as e:
            print(e) 
            return JsonResponse({'message':'El producto no existe'})
        val = request.data.get('status',None)
        print(val, 244)
        if val != None:
            if request.data['status'] == True:
                product.needChecker = False
                solic.status = 'active'
            elif request.data['status'] == False:
                product.needChecker = True
                solic.status = 'canceled'
        else: 
            return JsonResponse({'response':'invalido'}, status=400)
        solic.save()
        product.save()
        return JsonResponse({'succes':True})

class ReportView(viewsets.ModelViewSet):
    def post_report(self, request, pkP):
        serializer = ReportSerializer(data=request.data, context={'request':request,'idTransact':pkP})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=200)
        

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated,IsGroupAccepted]

    #GET all Categories
    def nested_list_categories(self, request):
        formC = request.GET.get('formC', None)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request':request})
        newSubC=[]
        if formC:
            for item in serializer.data:
                for subC in item['subCategories']:
                    if subC['purchased']:
                        newSubC.append(subC)
                item['subCategories'] = newSubC
                newSubC = []
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
        userPermision = uti.hasOrNotPermission(self, request, self, authClass=[IsAdmin])
        if not userPermision['IsAdmin']:
            return JsonResponse({'message':'No tienes acceso a esta vista'})
        userPermision = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin])
        if not userPermision['IsAdmin']:
            return JsonResponse({'message':'No esta autorizado para esto'},status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return JsonResponse(serializer.data, status=200)

    # POST One subcategory
    def post_subCategorie(self, request, *args, **kwargs):
        value = self.get_object()
        userPermision = uti.hasOrNotPermission(self, request, self, authClass=[IsAdmin])
        if not userPermision['IsAdmin']:
            return JsonResponse({'message':'No tienes acceso a esta vista'})
        serializer = SubCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        
        newSub = SubCategory(category=value, **validated_data)
        newSub.save()
        categoryObj = Category.objects.get(id=value.id)
        serializer = self.get_serializer(categoryObj)
        return JsonResponse(serializer.data, status=200)
    
    def update_subCategory(self, request, subCat_id, *args, **kwargs):
        userPermision = uti.hasOrNotPermission(self, request, self, authClass=[IsAdmin])
        if not userPermision['IsAdmin']:
            return JsonResponse({'message':'No tienes acceso a esta vista'})
        print(subCat_id)
        try:
            subObj= SubCategory.objects.get(id=subCat_id)
        except SubCategory.DoesNotExist:
            return JsonResponse({'detail':'No existe'}) 

        serializer = SubCategorySerializer(subObj, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()   
        return  JsonResponse(serializer.data)
    
    def delete_subCategory(self, request, subCat_id, *args, **kwargs):
        print(subCat_id)
        userPermision = uti.hasOrNotPermission(self, request, self, authClass=[IsAdmin])
        if not userPermision['IsAdmin']:
            return JsonResponse({'message':'No tienes acceso a esta vista'})
        try:
            subObj= SubCategory.objects.get(id=subCat_id)
        except SubCategory.DoesNotExist:
            return JsonResponse({'detail':'No existe'}) 
        print(subObj)
        subObj.delete()
        return JsonResponse({'message':'Campo borrado exitosamente'})
    
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


class SolicCheckerView(viewsets.ModelViewSet):
    queryset = CheckerSolic.objects.all()
    authentication_classes = [authentication.TokenAuthentication]

    def get_solic_checker(self, request):
        pending = request.GET.get('pending', None)
        cancel = request.GET.get('canceled',None)
        approved = request.GET.get('approved',None)

        if pending:
            objects = CheckerSolic.objects.filter(status = 'pending')
        elif cancel:
            objects = CheckerSolic.objects.filter(status = 'canceled')
        elif approved:
            objects = CheckerSolic.objects.filter(status = 'active')
        else: 
            objects = CheckerSolic.objects.all()

        serializer = SolicCheckerSerializer(objects, many=True)
        return JsonResponse(serializer.data,safe=False)
    
    def post_solic_checker(self, request,pk):
        try:
            product = ProductDigit.objects.get(id=pk)
            user= User.objects.get(id=request.user.id)
        except:
            return JsonResponse({'error':'El producto no existe'},status=404)
        if CheckerSolic.objects.filter(product_id=product.id).exists():
            print("122313")
            product.no_solicitud += 1
            product.save() 
            return JsonResponse({'no_solicitudes':product.no_solicitud})
        newObj = CheckerSolic(product=product, status='pending', user=user)
        newObj.save()
        serializer = SolicCheckerSerializer(newObj)
        print(serializer.data)
        return JsonResponse(serializer.data,status=201)



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
            print(instances[0].is_superuser,"229")
        serializer  = UserSerializer(instances, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
        
    def post_user(self, request, *args, **kwargs):
        serializer = UserCreatorSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        serializerRep = UserSerializer(user)   
        return JsonResponse(serializerRep.data, status=200)

    def put_user_data(self, request, *args, **kwargs):
        roles=request.GET.get('roles','false')
        
        userObj = self.get_object()
        userPermision = uti.hasOrNotPermission(self, request, self, authClass=[IsAdmin, IsSeller,IsChecker, IsBuyer], oneObj=True, obj=userObj)
        print(userPermision)
        if not any(val is True for val in userPermision.values()):
            return JsonResponse({"message":"No tiene acceso a este objeto",'ID':request.user.id})
        if not userPermision['IsAdmin'] and roles=='true':
            return JsonResponse({'message':'No tiene permiso para esta funcion'}, status=403)
        # print(roles)
        print(request.data)
        serializer = UserCreatorSerializer(userObj,data=request.data, partial=True, context={"roles":roles, 'update':True, 'request':request})
        
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        serializer= UserSerializer(userObj)
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
        result = serializer.data
        return JsonResponse(result, status=200)


    # DELETE one User
    def delete_user(self, request, *args, **kwargs):
        instance=self.get_object()
        userPermision = uti.hasOrNotPermission(self, request, self, authClass=[IsAdmin],oneObj=True,obj=instance)
        print(userPermision, 280)
        if not userPermision['IsAdmin']:
            return JsonResponse({'message':'Largo de aqui'}, status=403)
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
        print(dataAuth)
        token = dataAuth.split(' ')[1]
        token1 = Token.objects.filter(key=token).first()
        print(type(token1))
        token1.delete()
        return JsonResponse({'message':'Token Borrado Exitosamente'}, status=200)
    
class AuthenticationView(ObtainAuthToken):
    serializer_class = AuthenticationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {'token': token.key, 'user':user.id, 'D_A':user.is_superuser}
        return JsonResponse(data)


class TransactsView(viewsets.ModelViewSet):
    queryset = Transacts.objects.all()
    serializer_class = TransactsSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = []
    

    def get_all_transacts(self, request):
        isDigital = request.GET.get('digitals',None)
        isFisic = request.GET.get('fisics',None)
        widthPage = request.GET.get('pw', 12)
        pTransact = request.GET.get('pt',None)
        print(isFisic, pTransact)
        if isFisic and pTransact:
            print(request.user.id,548)
            transacts = Transacts.objects.filter(productFisic__isnull=False, buyers=request.user.id).order_by(
                Case(
                    When(status='Procesando',then=1),
                    When(status='Aceptado',then=2),
                    When(status='Rechazado',then=3),
                    default=4
                )
            )
        elif isDigital and not pTransact:
            print(2)
            transacts = Transacts.objects.filter(productDigit__isnull=False).order_by('-dateTransact')
        elif isFisic:
            transacts = Transacts.objects.filter(productFisic__isnull=False,buyers=request.user.id).order_by('-dateTransact')
        else: 
            transacts = Transacts.objects.all()
        # userPermision = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin])
        # if not userPermision['IsAdmin']:
  
        paginator = Paginator(transacts, per_page=widthPage)
        page_number= request.GET.get('page',1)
        if int(page_number) > paginator.num_pages:
            return JsonResponse({"error":"No hay mas paginas"}, status=404)
        paginated_data = paginator.get_page(page_number)
        print(paginated_data[0]) 
        serializer= TransactsSerializer(paginated_data, many=True, context={'request':request})
        print(paginated_data,2)
        dicc = {
            "actual_page": int(page_number),
            "available_pages":  paginator.num_pages - int(page_number),
            "data": serializer.data
        }
        return JsonResponse(dicc, status=200, safe=False)

    def post_transact_fisics(self, request):
        serializer = TransactsSerializer(data=request.data, context={'request':request, 'type':'fisics'})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return JsonResponse(serializer.data, status=201)
    
    def post_transact_digits(self, request):
        serializer = TransactsSerializer(data=request.data, context={'request':request, 'type':'digitals'})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return JsonResponse(serializer.data, status=201)
    
    def post_new_transacts_method(self, request):
        serializer = TransactsSerializer(data=request.data, context={'request':request, 'type':'method'})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return JsonResponse(serializer.data, status=201)

    def put_transact(self, request, pk): 
        try:
            obj = Transacts.objects.get(id=pk)
            print(obj)
            serializer = TransactsSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else:
                return JsonResponse({'error':'Sintaxis incorrecta'}, status=400)
            
            return JsonResponse(serializer.data, status=200)
            
        except Exception as e: 
            print(e)
            return JsonResponse({'error':'El producto no existe'}, status=404)
            
    def delete_transact(self, request, *args, **kwargs):
        transact = self.get_object()
        if transact.status == 'Procesando':
            self.perform_destroy(transact)
            return JsonResponse({'message':'Transaccion eliminada exitosamente'},status=204)
        else:
            return JsonResponse({'mE':'No puedes borrar esto'})

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
    permission_classes = [IsAuthenticated]

    def get_invitation_codes(self, request):
        invCodes = InvitationCodes.objects.all()
        result = InvitationCodesSerializer(invCodes, many=True).data
        return JsonResponse(result, status = 200, safe=False)
    
    def get_invitation_code_user_based(self, request, pk):
        user = User.objects.get(id=pk)
        invCodes = InvitationCodes.objects.filter(created_by=user)
        result = InvitationCodesSerializer(invCodes, many=True).data
        return JsonResponse(result, status = 200, safe=False)

    def post_invitation_code(self, request):
        invitation = InvitationCodesSerializer(data=request.data, context={'request':request})
        if invitation.is_valid(raise_exception=True):
            try:
                values = invitation.save()
                result = InvitationCodesSerializer(values).data
            except:
                invitation = InvitationCodesSerializer(data=request.data, context={'request':request, 'error':True})
                invitation.is_valid(raise_exception=True)
                values = invitation.save()
                result = InvitationCodesSerializer(values).data
                return JsonResponse(result, status=201)
            return JsonResponse(result, status=201)
        return JsonResponse({"success":False},status=400)

    def delete_invitation_code(self, request, *args, **kwargs):
        InvitationCode = self.get_object()
        self.perform_destroy(InvitationCode)
        return JsonResponse({'detail':'Codigo de invitacion eliminado correctamente'}, status=200)

class RoleRequestsView(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated,IsGroupAccepted]
    serializer_class = RoleRequestsSerializer

    def get_role_requests(self, request):
        still = False if request.GET.get('still','false') == 'true' else True
        is_pass = True if request.GET.get('isPass', 'false') == 'true' else False
        userPerm = uti.hasOrNotPermission(self, request, self.__class__, authClass=[IsAdmin])
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
