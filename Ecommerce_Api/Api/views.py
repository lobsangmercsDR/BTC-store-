from rest_framework.views import APIView
from django.http import response
from operator import itemgetter
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
from rest_framework.decorators import authentication_classes, permission_classes


from django.http import HttpResponse
from .models import ProductFisic,MethodProducts,Withdrawals,Deposits,ReportTransacts,GenData,Stores,CheckerSolic,TransactCategories,ProductDigit,Category,Transacts,User,InvitationCodes, SubCategory
from .serializers import (TransactsSerializer,
                          TransactsViewAdminSerializer,
                          ResetPassSerializer,
                          DepositsSerializer,
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

class SearchAPIView(viewsets.ModelViewSet):
    def get(self, request):
        search_query = request.GET.get('query', '')
        product_type = request.GET.get('tip', '')
        subcategory = request.GET.get('subC', None) 
        if product_type.lower() == 'digitales':
            digit_results=None
            if subcategory:
              digit_results = ProductDigit.objects.filter(name__icontains=search_query, subCategory_id=subcategory)  
            else:
                digit_results = ProductDigit.objects.filter(name__icontains=search_query)
            digit_serializer = ProductDigitSerializer(digit_results, many=True)
            return JsonResponse(digit_serializer.data, safe=False)
        
        if product_type.lower() == 'fisicos':
            fisic_results=None
            if subcategory:
              fisic_results = ProductFisic.objects.filter(name__icontains=search_query, subCategory_id=subcategory)  
            else:
                fisic_results = ProductFisic.objects.filter(name__icontains=search_query)
            fisic_serializer = ProductSerializer(fisic_results, many=True)
            return JsonResponse(fisic_serializer.data, safe=False)
        
        if product_type.lower() == 'metodos':
            method_results=None
            if subcategory:
              method_results = ProductDigit.objects.filter(name__icontains=search_query, subCategory_id=subcategory)  
            else:
                method_results = ProductDigit.objects.filter(name__icontains=search_query)
            method_serializer = MethodSerializer(method_results, many=True)
            return JsonResponse(method_serializer.data,safe=False)
        
        fisic_results = ProductFisic.objects.filter(name__icontains=search_query)
        digit_results = ProductDigit.objects.filter(name__icontains=search_query)
        method_results = MethodProducts.objects.filter(name__icontains=search_query)
        
        fisic_serializer = ProductSerializer(fisic_results, many=True)
        digit_serializer = ProductDigitSerializer(digit_results, many=True)
        method_serializer = MethodSerializer(method_results, many=True)
        
        results = fisic_serializer.data + digit_serializer.data + method_serializer.data
        
        return JsonResponse(results, safe=False)

class WithDrawView(viewsets.ModelViewSet):
    queryset = Withdrawals.objects.all()
    serializer_class = WithDrawSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_admin_withdraws(self, request):
        type = request.GET.get('t', None)
        print(type)
        if type:
            if type == "pending":
                objects = Withdrawals.objects.filter(status="Pendiente")
            elif type == "approved":
                objects = Withdrawals.objects.filter(status="Aprobada")
            elif type == "declined":
                objects = Withdrawals.objects.filter(status="Rechazada")
            else:
                objects = Withdrawals.objects.all()
        else:
            objects = Withdrawals.objects.all()
        serializer = WithDrawSerializer(objects, many=True)
        return JsonResponse(serializer.data, status=200,safe=False)
    
    def get_withdraws(self, request):
        objects = Withdrawals.objects.filter(user=request.user.id).order_by('id')
        paginator = Paginator(objects, per_page=5)
        page_rq_num = request.GET.get('pg',1) 
        page = paginator.get_page(page_rq_num)
        serializer = WithDrawSerializer(page, many=True)
        further = False if int(page_rq_num) >= paginator.num_pages else True
        back = False if int(page_rq_num) ==1 else True 
        result = {
            'act_page': page_rq_num,
            'back': back, 
            'fur':further,
            'page':serializer.data
        }
        return JsonResponse(result, status=200, safe=False)

    def post_new_withdraw(self, request):
        data = request.data
        user = request.user
        serializer = WithDrawSerializer(data=data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    
    def put_withdraw_status(self, request, id):
        approve= request.GET.get('approve',None)
        try:
                withdraw = Withdrawals.objects.get(id=id)
        except Exception as e:
            print(e)
            JsonResponse({'msg':'Retiro no existente'}, status=404)

        if approve:
            withdraw.status= "Aprobada"
            withdraw.fecha_review = datetime.now()
            withdraw.user.userBalance -= withdraw.amount
            withdraw.user.save()
            withdraw.save()
        else:
            withdraw.status="Rechazada"
            withdraw.fecha_review = datetime.now()
            withdraw.save()
        return JsonResponse({'msg':'Actualizacion realizada con exito'})

class DepositView(viewsets.ModelViewSet):
    queryset = Deposits.objects.all()

    def get_admin_deposits(self, request):
        queryset= Deposits.objects.all()
        serializer = DepositsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post_deposit(self, request):
        serializer = DepositsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)

class Img_view(viewsets.ModelViewSet):
    def get_file_img(self, request, image_name):
        pathFile = os.path.abspath(__file__)
        path = pathFile.replace(r"Api\views.py", "") + r"images" + '\\' + image_name   
        print(path)
        if os.path.exists(path=path):
            return FileResponse(open(path,'rb'),content_type='image/jpeg')
        else:
            print('ruta')
            return JsonResponse({'error':'No se encuentra la imagen'}, status=404)
        
    def put_file_img(self, request, image_name):
        localD = os.path.abspath(__file__)
        print(image_name,4)
        TP_route = localD.replace(r"Api\views.py", "") +"\images" 
        file_img = os.path.join(TP_route, image_name)
        img_product = request.data['image_product']

        if not os.path.exists(file_img):
            return JsonResponse({"error":"La imagen no existe"}, status=400)
        with open(file_img, 'wb') as f:
            for chunk in img_product.chunks():
                f.write(chunk)


        
        return JsonResponse({'message':'imagen guardada'})

    def get_img_banner(self, request, img_name):
        pathFile = os.path.abspath(__file__)
        path = pathFile.replace(r"Api\views.py", "") + r"images" + '\\store\\bann\\' + img_name   
        if os.path.exists(path=path):
            return FileResponse(open(path,'rb'),content_type='image/jpeg')
        else:
            print('ruta')
            return JsonResponse({'error':'No se encuentra la imagen'}, status=404)
    
    def get_img_avatar(self, request, img_name):
        pathFile = os.path.abspath(__file__)
        buildPath = pathFile.replace("Api\\views.py", "") + "\\images\\store\\avt\\" + img_name
        print(buildPath)
        if os.path.exists(path=buildPath):
            return FileResponse(open(buildPath, 'rb'), content_type='image/jpeg')
        else:
            return JsonResponse({'error':'No se encuentra la imagen'}, status=404)


class StoreView(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes= [IsAuthenticated]

    def get_store_user_based(self, request, pk):
        try:
            store = Stores.objects.get(seller_id=pk)
            print(request.user.id,22)
            serializer = StoreSerializer(store, context={'request':request})
            return JsonResponse({'success':True,'store':serializer.data})
        except Exception as  e:
            print(e,'error')
            return JsonResponse({'success':False,'msg':'Store no encontrada'}, status=404)

    def create_store(self, request):
        serializer = StoreSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)

class TransactSubcategoryView(viewsets.ModelViewSet):
    queryset = TransactCategories.objects.all()
    serializer_class = TransactCategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, IsGroupAccepted]
    
    def get(self, request):
        transactse= TransactCategories.objects.all()
        serializer = TransactCategorySerializer(transactse, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    def delete_user_based(self, request, id):
        checker = request.GET.get('checker','f')
        if checker == 't':
            transactsQueryset = TransactCategories.objects.filter(subCategory__nameSubCategory='Checker', user=id)
            if transactsQueryset:
                transactsQueryset.delete()
            return JsonResponse({'msg':'Accion realizada con exito'})
        transactsQueryset = TransactCategories.objects.filter(user=id)
        if len(transactsQueryset) >0:
            transactsQueryset.delete()
            return JsonResponse({'msg':'Accion realizada con exito'})
        else:
            raise serializers.ValidationError({'msg':'El usuario no tiene transacciones con categorias'})

        

    def post(self, request):
        serializer = TransactCategorySerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        transSub = serializer.save()
        print(transSub.subCategory.nameSubCategory , 2222)
        user = User.objects.get(id=request.user.id)
        if UserSerializer(user).data['group'] == "buyers" and transSub.subCategory.nameSubCategory != "Checker":
            group = Group.objects.get(name='sellers')
            user.groups.set([group])
            user.save()
        if UserSerializer(user).data['group'] == "buyers" and transSub.subCategory.nameSubCategory == "Checker":
            group = Group.objects.get(name='checkers')
            user.groups.set([group])
            user.save()
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer=serializer)
        return JsonResponse(serializer.data, status=200)

class ProductView(viewsets.ModelViewSet):
    queryset = ProductFisic.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = Paginator
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = []

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
    
    def postMethod(self, request):
        serializer = MethodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=201)


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
        pSize = request.GET.get('p_size', 5)
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
        paginator = Paginator(products, per_page=pSize)
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
        


    def get_inventory(self, request):
        uti.checkAuth(request, raise_exception=True)
        groups = uti.checkAdminSeller(request)
        isPaginated = request.GET.get('paginated',"f")
        own = request.GET.get('own',"f")
        if 'sellers' in groups:
            own = "t"
        if own =="t":
            store = Stores.objects.get(seller=request.user.id)
            querysetFisic = ProductFisic.objects.filter(store=store, ) 
            querysetDigit = ProductDigit.objects.filter(store=store) 
            querysetMethod = MethodProducts.objects.filter(store=store) 
        else:
            querysetFisic  = ProductFisic.objects.all()
            querysetDigit = ProductDigit.objects.all()
            querysetMethod = MethodProducts.objects.all()
        print(querysetDigit, querysetFisic, querysetMethod, 123132)
        serialized_Fisic = ProductSerializer(querysetFisic, many=True).data
        serialized_Digit = ProductDigitSerializer(querysetDigit, many=True).data
        serialized_Method = MethodSerializer(querysetMethod, many=True).data

        combined_data = serialized_Fisic + serialized_Digit + serialized_Method
        sorted_data  = sorted(combined_data,key=itemgetter('dateCreated'))
        if isPaginated == "t":
            page = request.GET.get("page", 1)
            paginator = Paginator(sorted_data, 5)

            try:
                Actpage = paginator.page(page)
                return JsonResponse({
                            "items":list(Actpage),
                            "act_page":Actpage.number,
                            "rest_pages":paginator.num_pages - int(Actpage.number)
                             }, status=200)
            except Exception as e:
                return JsonResponse({"error":"Page Invalid"})
        else:
            return JsonResponse({"items":sorted_data, "is_paginated":False})
      

    # POST a new product (Taking Seller id)
    def post_product(self,request):
        serializer = ProductSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.get_success_headers(serializer.data)
        return JsonResponse(serializer.data, status=200)
 
    # PUT a product created by a seller
    def update_product(self, request,*args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return JsonResponse({'message':'El campo ha sido actualizado','result':serializer.data, 'status':200}, status=200)

    def delete_product(self, request, *args, **kwargs):
        instance= self.get_object()
        userPerm = uti.hasOrNotPermission(self, request,self, authClass=[IsSeller,IsAdmin],oneObj=True, obj=instance)
        print(userPerm)
        if not any(val is True for val in userPerm.values()):
            return JsonResponse({"message":"No tiene acceso a esta funcionalidad o producto"}, status=403)
        self.perform_destroy(instance)
        return JsonResponse({'message':'Objeto borrado con exito'})


    def check_permissions(self, request):
        print(self.action)
        if self.action == 'delete_product':
            print("asdsda")
            self.permission_classes = [IsAuthenticated]
        super().check_permissions(request)

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
        serializer = ProductDigitSerializer(paginated_data,context={'request':request}, many=True)
        return JsonResponse({'available_pages':paginator.num_pages-int(page_number),'page':int(page_number),'data':serializer.data}, status=200, safe=False)
    
    def get_digit_product(self, request, *args, pk):
        try:
            instance = ProductDigit.objects.get(id=pk)
            serializer = ProductDigitSerializer(instance)
            result = serializer.data
            return JsonResponse(result, status=200)
        except: 
            return JsonResponse({"error":"no existe"}, status=200)

    def put_digit_product(self, request, pk):
        try:
            instance = ProductDigit.objects.get(id=pk)
        except Exception():
            return JsonResponse({'error':'No existe el producto'})
        
        serializer = ProductDigitSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"message":"Exito", "object":serializer.data})

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
                product.comisionCheck = GenData.objects.first().price_checker
                solic.status = 'active'
            elif request.data['status'] == False:
                product.needChecker = True
                solic.status = 'canceled'
        else: 
            return JsonResponse({'response':'invalido'}, status=400)
        solic.save()
        product.save()
        return JsonResponse({'succes':True})
    
    def delete_digit_product(self, request, *args, **kwargs):
        instance= self.get_object()
        userPerm = uti.hasOrNotPermission(self, request,self, authClass=[IsSeller,IsAdmin],oneObj=True, obj=instance)
        print(userPerm)
        if not any(val is True for val in userPerm.values()):
            return JsonResponse({"message":"No tiene acceso a esta funcionalidad o producto"}, status=403)
        self.perform_destroy(instance)
        return JsonResponse({'message':'Objeto borrado con exito'})
    
    def check_permissions(self, request):

        if self.action == 'delete_digit_product':

            self.permission_classes = [IsAuthenticated]
        super().check_permissions(request)

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

class RestPassView(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def put_password(self, request):
        serializer = ResetPassSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        updateSer = ResetPassSerializer(user,data=request.data) 
        updateSer.is_valid(raise_exception=True)
        updateSer.save()
        return JsonResponse({'msg':'Accion realizada con exito'})

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
        product.no_solicitud += 1
        product.save() 
        newObj = CheckerSolic(product=product, status='pending', user=user)
        newObj.save()
        serializer = SolicCheckerSerializer(newObj)
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
        serializer = UserCreatorSerializer(userObj,data=request.data, partial=True, context={"roles":roles, 'update':True, 'request':request})        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({}, status=200)
    

    


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
    
    def put_password(self, request):
        serializer = ResetPassSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        updateSer = ResetPassSerializer(user,data=request.data) 
        updateSer.is_valid(raise_exception=True)
        updateSer.save()
        return JsonResponse({'msg':'Accion realizada con exito'})
    
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
    

    def get_admin_view_transacts(self, request):
        date_start = request.GET.get("dr_s",None)
        date_end = request.GET.get("dr_e",None)
        querySearch = request.GET.get("sq", None)
        own = request.GET.get('own', 'f')

        if date_start and date_end:
            start = datetime.strptime(date_start,  "%Y-%m-%dT%H:%M:%S.%fZ").date()
            end = datetime.strptime(date_end,  "%Y-%m-%dT%H:%M:%S.%fZ").date()
            queryset = Transacts.objects.filter(dateTransact__range=(start,end))
            if date_start == date_end:
                end = end + timedelta(days=1)
                queryset = Transacts.objects.filter(dateTransact__range=(start, end))
            print(queryset)
        else:
            if querySearch:
                queryset = Transacts.objects.filter(Q(productFisic__name__icontains=querySearch) | Q(productDigit__name__icontains=querySearch) | Q(methodProduct__name__icontains=querySearch))
            else:
                queryset = Transacts.objects.all()
        df = TransactsViewAdminSerializer(queryset, many=True)
        if own =="t": 
            print(2)
            result = list(filter(lambda item: item['product']['store']['seller']['id'] == request.user.id or item['buyers']['id'] == request.user.id,df.data ))
            print(request.user.id)
        else: 
            result = df.data
        return JsonResponse(result, safe=False)
        

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
                if serializer.validated_data['status'] == "Rechazado":
                    obj.buyers.userBalance += obj.productFisic.price
                    obj.buyers.save()
                serializer.save()
            else:
                return JsonResponse({'error':'Sintaxis incorrecta'}, status=400)
            
            return JsonResponse(serializer.data, status=200)
            
        except Exception as e: 
            print(e)
            return JsonResponse({'error':'El producto no existe'}, status=404)
            
    def delete_transact(self, request,pk):
        transact = self.get_object()
        if transact.status == 'Procesando':
            transact.buyers.userBalance += transact.total
            transact.buyers.save() 
            print(transact.buyers.userBalance,904)
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

    def validate_group(self, request, id):
        try: 
            user = User.objects.get(id=id)
        except Exception as e:
            print(e)
            return JsonResponse({'msg':'El usuario especificado no existe'})
        data = UserSerializer(user).data
        subCat = SubCategory.objects.get(nameSubCategory='Checker')
        checkerTrans = TransactCategories.objects.filter(user=id, subCategory=subCat).exists() 
        userTransct = TransactCategories.objects.filter(user=id)
        isSeller = userTransct.exclude(subCategory__nameSubCategory='Checker')
        print(userTransct)
        group = data['group']
        if group == 'SuperUser' or group== 'administrator':
            result = {'result':[]}
        if group == 'buyers':
            result = {'result':['buyers']}
        if group == 'sellers':
            result = {'result':['sellers']}
        if group == 'checkers' and checkerTrans:
            result = {'result':['checker']}
        if group == 'sellers' and checkerTrans:
            result = {'result':['sellers', 'checker']}
        if group=='checkers' and isSeller:
            result = {'result':['checker', 'sellers']}

        return JsonResponse(result)

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

class GeneralDataView(viewsets.ModelViewSet):
    queryset = GenData.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
     
    def get_secret_key(self, request):
        instance= GenData.objects.values()
        if len(instance) != 0:
            secKey = list(instance)[0]
            return JsonResponse({'sec_key':secKey})
        else:
            return JsonResponse({'err':'El sistema carece de secretKey'}, status=400)
        
    def get_graphics_data(self, request):
        dateSt = request.GET.get('stDate')
        dateEd = request.GET.get('edDate')
        trans_ins = Transacts.objects.first()
        user_ins = User.objects.first()

        if dateSt and dateEd: 
            dateSt = datetime.strptime(dateSt, '%Y-%m-%dT%H:%M:%S.%fZ')
            dateEd =datetime.strptime(dateEd, '%Y-%m-%dT%H:%M:%S.%fZ')
            currDate = dateSt
            print(dateSt, dateEd)
            result  = {
                "total_shares": [],
                "total_cnt_shares": [],
                "total_users":[]
            } 
            while currDate < dateEd:
                result['total_shares'].append(trans_ins.total_transacts_amount(date=currDate))
                result['total_cnt_shares'].append(trans_ins.total_num_shares(date=currDate))
                result['total_users'].append(user_ins.total_registered(date=currDate))
                currDate +=timedelta(days=1)
                print(currDate)

        return JsonResponse({"msg":"success", 'result':result})


        totalShares = trans_ins.total_transacts_amount()
        totalNumShares = trans_ins.total_num_shares(all=True)
        totalUsersCreated = user_ins.total_registered(all=True)

    def put_secret_key(self, request):
        try:
            instance= GenData.objects.get(id=1)
            instance.secret_key = request.data['secret_key']
            instance.save()
            return JsonResponse({'msg':'listo'})
        except Exception as e:
            print(e)
            return JsonResponse({'msg':'La secret key no existe o sus datos son invalidos'}, status=404)
    
    def get_comision_checker(self, request):
        instance = GenData.objects.first()
        if instance:
            return JsonResponse({'priceCheker':instance.price_checker})
        else:
            return JsonResponse({'msg':'price error'},status=404)

    def general_data(self, request):
        all = request.GET.get('all')
        instance = Transacts.objects.first()
        user = User.objects.first()
        totalShares = 0
        totalNumShares = 0
        totalUsersCreated = 0
        if all== 't':
            totalShares = instance.total_transacts_amount(all=True)
            totalNumShares = instance.total_num_shares(all=True)
            totalUsersCreated = user.total_registered(all=True)
        else:
            totalShares = instance.total_transacts_amount()
            totalNumShares = instance.total_num_shares()
            totalUsersCreated = user.total_registered()
        return JsonResponse({'total_shares':totalShares,'total_num_shares':totalNumShares, 'usersAdded':totalUsersCreated})