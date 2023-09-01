from django.forms import ValidationError

from rest_framework import serializers,exceptions
from .models import Category, ProductFisic, ProductDigit,ReportTransacts,Deposits, Withdrawals, TransactCategories, CheckerSolic, Transacts,MethodProducts,User,InvitationCodes, SubCategory, Stores
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from .utils import services as uti
import random
import requests as rq
import string

dateFormat = "%d/%m/%Y %I:%M:%S %p"

class GroupsSerializer(serializers.Serializer): 
    class Meta:
        model = Group
        fields = ['id','name','users_count']
       

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id'] = instance.id
        rep['name'] = instance.name
        rep['user_count'] = self.get_users_count(instance)
        return rep

    def get_users_count(self, obj):
        count = obj.user_set.count()
        return count
     
class UserNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model= get_user_model()
        fields = ['id','name','is_superuser']

class UserSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()
    last_login = serializers.DateTimeField(format="%d/%m/%Y %I:%M:%S %p")
    createdAt = serializers.DateTimeField(format="%d/%m/%Y")
    purchases_count = serializers.SerializerMethodField()
    
    class Meta:
        model = get_user_model() 
        extra_kwargs = {'password':{'write_only':True}}
        fields = ['id','email','password','name','userBalance','phoneNumber','direction','wallet_address','createdAt','is_active','group', 'last_login', 'purchases_count']
        ref_name = 'UserSerializer'

    def get_purchases_count(self, obj):
        return obj.purchases_count()

 
    def get_group(self, obj):
        print(obj.groups, "59")
        if obj.is_superuser:
            return "SuperUser"
        elif obj.is_active== False:
            return False
        else:  
            return list(obj.groups.values_list('name',flat=True))[0]

class StoreSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    seller = UserNestedSerializer()

    class Meta:
        model = Stores
        fields = ['id', 'nameStore','seller','product_count']
    
    def get_product_count(self, obj):
        count = obj.product_count 

class DepositsSerializer(serializers.ModelSerializer):
    user = UserNestedSerializer(required=False)

    class Meta:
        model = Deposits
        fields = ('id', 'no_orden', 'user', 'tasaDepositMoment', 'quantityUSD', 'status', 'date')

class WithDrawSerializer(serializers.ModelSerializer):
    user = UserNestedSerializer(required=False)


    def validate_amount(self, obj):
        user = self.context.get('request').user
        if user.userBalance < int(obj):
            raise serializers.ValidationError('No tiene suficiente balance para esta transaccion')
        return obj

    class Meta:
        model = Withdrawals
        fields = ['id','no_orden','amount','status','fecha_solicitud','fecha_review','walletRequested','user']

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        validated_data['status'] = 'Pendiente'
        return super().create(validated_data)

class InvitationCodesSerializer(serializers.ModelSerializer):
    expire_date = dateFormat
    created_at = serializers.DateTimeField(format="%d/%m/%Y %I:%M:%S %p",required=False)
    created_by = UserNestedSerializer(read_only=True)
    countUsers = serializers.IntegerField(read_only=True)
    class Meta:
        model = InvitationCodes
        fields=['id','invitationCodes','description','is_expired','countUsers','created_at','created_by','expire_date']

    def create(self, validated_data):
        request = self.context.get('request')
        newCode = uti.generate_invitation_code()
        print(request)
        ActualUserId = request.user.id
        ActualUser = User.objects.get(id=ActualUserId)
        print(ActualUser)
        if self.context.get('error'):
            InvitationCode = InvitationCodes.objects.create(invitationCodes=newCode, created_by=ActualUser, **validated_data)
            print("asasa")
            return InvitationCode
        else:
            InvitationCode = InvitationCodes.objects.create(created_by=ActualUser, **validated_data)
            return InvitationCode

class MethodSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    transacts_count = serializers.SerializerMethodField()
    subCategory = serializers.SerializerMethodField()
    dateCreated = serializers.DateTimeField(required=False,format=dateFormat)
    store_id = serializers.IntegerField()

    class Meta:
        model = MethodProducts
        fields = ['id','name', 'dateCreated','actQuantity','quantity','subCategory','sendDirection','description','price','store','image','transacts_count', 'store_id']


    def get_transacts_count(self, obj):
        return obj.transacts_count

    def get_subCategory(self, obj):
        return {
            'category':'Method',
            'nameSub':'N/A'
        }
    
    def create(self, validated_data):
        store_id = validated_data.pop('store_id')
        method = MethodProducts.objects.create(store_id=store_id, **validated_data)
        return method

class UserCreatorSerializer(serializers.ModelSerializer):
    add_group = serializers.CharField(read_only=True)
    delete_group= serializers.CharField(read_only=True)
    invitation_code = serializers.CharField()
    name = serializers.CharField(required=True)
    confirm_pass = serializers.CharField(write_only=True)
    createdAt = serializers.DateField(read_only=True)
    invitation_code = serializers.CharField(write_only=True)

    def validate_invitation_code(self, value):
        invitationObj = InvitationCodes.objects.filter(invitationCodes=value).first()
        if invitationObj ==None:
            raise serializers.ValidationError("No encontrado")
        elif invitationObj.is_expired == True:
            raise serializers.ValidationError("Codigo de invitacion expirado")
        return value

    def validate(self, data):
        if not self.context.get('update'):
            if data['password'] != data['confirm_pass']:
                raise serializers.ValidationError({'confirm_pass':'Sus contraseñas no coinciden'})
            print(data)
        return data        

    class Meta:
        model = get_user_model() 
        fields = ['id','email','password','confirm_pass','name','is_active','add_group', 'invitation_code', 'delete_group','createdAt']
        extra_kwargs = {'password': {'write_only': True}}
        ref_name = 'UserCreatorSerializer'

    def create(self, validated_data):
        group_name = ["buyers"]
        invitation_code = validated_data.pop('invitation_code',None)
        validated_data.pop('confirm_pass')
        if invitation_code:
            invitationObj = InvitationCodes.objects.get(invitationCodes=invitation_code)
            invitationObj.countUsers += 1
            invitationObj.save()
        username = validated_data['name']
        formData = {
        "api_key": "8e63-14fd-610e-6b45",
        "label": username,
        "currency": "btc"
        }
        
        group = Group.objects.get(name=group_name[0]) 
        resp= rq.post('https://block.io/api/v2/get_new_address', data=formData)
        print(resp.content)
        if resp.status_code == 200:
            dictionary = dict(resp.json())
            validated_data['wallet_address'] = dictionary['data']['address']
        else:
            raise serializers.ValidationError({'message':"No se ha podido crear su cartera, espere"})
        user = User.objects.create_user(**validated_data)
        user.groups.add(group)

        
        return user

    def update(self, instance,validated_data):
        validated_data = self.context['request'].data   
        group_name = validated_data.pop('add_group', False)
        delete_group = validated_data.pop('delete_group', False)
        change_group = validated_data.pop('change_group', False)
        not_found_groups = []
        if change_group == "SuperUser":
            print(145)
            instance.groups.set([])
            return super().update(instance, validated_data)
        if change_group:
            try:    
                group = Group.objects.get(name=change_group)
            except Group.DoesNotExist:
                not_found_groups.append(change_group)
            if not_found_groups:
                message = f"Groups {', '.join(not_found_groups)} not found"
                raise serializers.ValidationError(message, code=400)
            instance.groups.set([group])

        evidence= True if "is_active" in validated_data.keys() or "group" in validated_data.keys() or "group_name" in validated_data.keys()  or "password" in validated_data.keys() else False
        roles = True if self.context.get('roles') == 'true' else False
        if not roles and evidence:
            raise serializers.ValidationError({"message":"Acceso a estas propiedades no tienes"})
        groups = []
        if group_name: 
            try:
                group = Group.objects.get(name=group_name)
                groups.append(group)
            except Group.DoesNotExist:
                not_found_groups.append(group_name)
            if not_found_groups:
                message = f"Groups {', '.join(not_found_groups)} not found"
                raise serializers.ValidationError(message, code=400)
            instance.groups.add(group)

        if delete_group:
                try:
                    groupIns = Group.objects.get(name=delete_group)
                except:
                    raise serializers.ValidationError(f"Grupo {delete_group} no existe")
                instance.groups.remove(groupIns)
        deleteList = ['last_login', 'wallet_address','createdAt']
        for item in deleteList:
            del validated_data[item]
        return super().update(instance, validated_data)
            

class SubCategorySerializer(serializers.ModelSerializer):
    purchased = serializers.SerializerMethodField()

    
    class Meta:
        model = SubCategory
        fields = ['id', 'nameSubCategory','priceSubCategory', 'purchased','minPriceBTC','maxPriceBTC']

    def get_purchased(self, obj):
        idUser = self.context['request'].user.id
        print(idUser)
        hasPurchased = TransactCategories.objects.filter(user_id=idUser, subCategory=obj.id).exists()
        if hasPurchased:
            return True
        else:
            return False
        
class ExtSubCategorySerializer(serializers.ModelSerializer):

    
    class Meta:
        model = SubCategory
        fields = ['id', 'nameSubCategory','priceSubCategory','minPriceBTC','maxPriceBTC']

class ProductDigitSerializer(serializers.ModelSerializer):
    dateCreated = serializers.DateTimeField(format="%d/%m/%Y %I:%M %p", required=False)
    subCategory = serializers.SerializerMethodField()
    subCategory_id = serializers.IntegerField(required=True)
    store = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()


    def get_id(self, obj):
        return f'2.{obj.id}'

    def get_quantity(self, obj):
        result= 'Available'
        return result

    def get_subCategory(self, obj):
        result =  {
            "id":obj.subCategory.id if obj.subCategory != None else None,
            "nameSub":obj.subCategory.nameSubCategory if obj.subCategory != None else None,
            "category":"Digitales"
        }
        return result    

    def get_store(self, obj):
        store = Stores.objects.get(id=obj.store_id)
        serializer = StoreSerializer(store)
        return serializer.data

    def validate_price(self, value):
        if value == 0:
            raise serializers.ValidationError("El precio no puede ser 0")
        return value

    class Meta:
        model = ProductDigit
        fields = ['id', 'name', 'price','no_solicitud','subCategory','quantity','subCategory_id', 'description','comisionCheck','aditional_details','needChecker', 'dateCreated','store','checkerText']

    def create(self, validated_data):
        request = self.context.get('request',None)
        subC_id = validated_data.pop('subCategory_id')
        subObj = SubCategory.objects.get(id=subC_id)
        store = Stores.objects.get(seller=request.user.id)
        instance = ProductDigit.objects.create(store=store, subCategory=subObj, **validated_data)
        return instance

class TransactCategorySerializer(serializers.ModelSerializer):
    dateTransact = serializers.DateTimeField(format=dateFormat, required=False)
    user = UserSerializer(read_only=True)
    subcategory_id = serializers.IntegerField(write_only=True)
    subCategory = SubCategorySerializer(read_only=True)
    
    class Meta:
        model = TransactCategories
        fields = ['id', 'subCategory','subcategory_id','user','dateTransact']



    def validate_subcategory_id(self, value):
        subcategory = SubCategory.objects.filter(id=value).exists()
        if subcategory:
            return value
        else:
            raise serializers.ValidationError("No existe")

    def create(self, validated_data):
        userBuyer = self.context['request'].user  # Obtener el usuario actual
        subcategory = validated_data.get('subcategory_id',None)
        print(userBuyer)
        print(subcategory)
        subcategoryObj = SubCategory.objects.get(id=subcategory) 
        userCreator = subcategoryObj.userCreator

        if userBuyer.userBalance >= subcategoryObj.priceSubCategory:
                userBuyer.userBalance -= subcategoryObj.priceSubCategory
                userCreator.userBalance += subcategoryObj.priceSubCategory
                userBuyer.save()
                userCreator.save()
                print(dir(TransactCategories()))  
                # Crear la transacción y guardarla en la base de datos
                transact = TransactCategories(
                    user=userBuyer,
                    subCategory=subcategoryObj,
                )
                transact.save()

                return transact
        else:
            raise serializers.ValidationError("Saldo insuficiente para realizar la transacción.")

class CategorySerializer(serializers.ModelSerializer): 
    subCategories = serializers.SerializerMethodField()
    class Meta:
        model = Category 
        fields =  ['id','nameCategory', 'subCategories']
    


    def get_subCategories(self, obj):
        request = self.context.get('request', None)
        subCategories = SubCategory.objects.filter(category=obj.id)
        return SubCategorySerializer(subCategories, many=True,context=self.context).data

class CategoryWithoutProductsSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category 
        fields =  ['id','nameCategory','product_count']
        
        def get_product_count(self,obj):
            count = obj.products_quantity
            return count

class CategoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','nameCategory']

class ProductSerializer(serializers.ModelSerializer):
    seller = UserNestedSerializer(read_only=True)
    category = CategoryNestedSerializer(read_only=True)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=10,decimal_places=2)
    image = serializers.ImageField(required=True, write_only=False)
    subCategory = serializers.SerializerMethodField()
    subCat_id = serializers.IntegerField(write_only=True)
    brand = serializers.CharField(required=True)
    aditional_details = serializers.CharField(required=True)
    id = serializers.SerializerMethodField()
    store = StoreSerializer(read_only=True)
    store_id = serializers.IntegerField()


    def get_id(self, obj):
        return f'1.{obj.id}'

    def validate_subCat_id(self, value):
        if not value: 
            raise serializers.ValidationError("No se proporcionó ninguna subcategoría")
        subObj = SubCategory.objects.filter(id=value).first()
        if not subObj:
            print("test")
            raise serializers.ValidationError("La sub categoria planteada no existe")
        return value
    
    def validate_image(self, value):
        print(value)
        if value==None:
            raise serializers.ValidationError("Este campo no debería estar vacío")
        return value

    def validate_quantity(self, value): 
        if value==0:
            raise serializers.ValidationError("El numero no puede ser 0")
        return value
    
    def validate_priceProduct(self, value):
        if value==0:
            raise serializers.ValidationError("Ingrese un valor valido")
        return value

    def get_price(self, obj):
        print(obj.priceProduct)
        return f"{obj.priceProduct}"

    def get_subCategory(self, obj):
        result =  {
            "id":obj.subCategory.id if obj.subCategory != None else None,
            "nameSub":obj.subCategory.nameSubCategory if obj.subCategory != None else None,
            "category":obj.subCategory.category.nameCategory if obj.subCategory != None  and obj.subCategory.category != None else None
        }
        return result

    class Meta:
        model = ProductFisic
        fields = [
                    'id',
                    'name',
                    'image',
                    'dateCreated',
                    'active',
                    'actQuantity',
                    'brand',
                    'aditional_details',
                    'seller', 
                    'quantity',
                    'address_direction',
                    'description',
                    'category',
                    'subCat_id',
                    'store',
                    'subCategory',
                    'aditional_details',
                    'price',
                    'store_id'
                ]

    

    def create(self, validated_data):
        subcId = validated_data.pop('subCat_id')
        storeId = validated_data.pop('store_id')
        subC = SubCategory.objects.get(id = subcId)
        store = Stores.objects.get(id = storeId)
        newProduct = ProductFisic.objects.create(subCategory=subC,store=store, **validated_data)
        return newProduct

    def update(self, instance, validated_data):
        userValidation= self.context.get('userPermision')
        if userValidation['IsChecker'] and not userValidation['IsAdmin'] and any( key != 'active' for key in validated_data.keys()):
            raise serializers.ValidationError({"message":"No puede editar esto"})
        print(validated_data) 
        return super().update(instance, validated_data)

class ProductNestedSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    
    class Meta:
        model = ProductFisic
        fields = ('id', 'name','price', 'store')

class ProductDigitNestedSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    
    class Meta:
        model = ProductDigit
        fields = ('id', 'name', 'price','store' )

class TransactProductNestedSerializer(serializers.ModelSerializer):
    seller = UserNestedSerializer(source='seller_id')

    class Meta:
        model = ProductFisic
        fields = ['id','nameProduct','priceProduct','dateReleased','active', 'seller']

class SolicCheckerSerializer(serializers.ModelSerializer): 
    dateCreated = serializers.DateTimeField(format="%d/%m/%Y %I:%M:%S %p")

    product = ProductDigitSerializer()
    class Meta: 
        model = CheckerSolic
        fields = ['id','product','dateCreated','status']

    def to_representation(self, instance):
        print(instance)
        result = super().to_representation(instance)
        return result

class TransactsSerializer(serializers.ModelSerializer):
    productDigit_id = serializers.IntegerField(write_only=True)
    quantity_asked = serializers.IntegerField(required=False)
    sendDirection = serializers.CharField(required=False)
    productDigit = ProductDigitSerializer(read_only=True)
    buyers = UserNestedSerializer(read_only=True)
    productFisic = ProductSerializer(read_only=True)
    dateTransact = serializers.DateTimeField(format="%m/%d/%Y %I:%M:%S %p", read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2,read_only=True)
    
    class Meta:
        model  = Transacts 
        fields = ['id','dateTransact','quantity_asked','status','total','sendDirection','productDigit','productFisic','buyers', 'productDigit_id', 'sendDirection','noSeguimiento','company']

    def create(self, validated_data):
        type = self.context.get('type') 
        product_id = validated_data.pop('productDigit_id', None)
        if not type == 'method' and not type == 'digitals':
            quantity_asked = validated_data['quantity_asked'] 
        
        request = self.context.get('request')
        buyer_id= request.user.id
        buyers = User.objects.get(id=buyer_id)
        total_price = 0
        try:
            if type == 'fisics':
                products = ProductFisic.objects.get(id=product_id)
                total_price = quantity_asked * products.price
            elif type=='method':
                products = MethodProducts.objects.get(id=product_id)
                total_price = products.price
            elif type == 'digitals':
                products = ProductDigit.objects.get(id=product_id)
                total_price = products.price + products.needChecker
        except Exception as e:
            print(e)
            raise serializers.ValidationError({"error":"Producto Inexistente"}) 
        print(total_price)
        user = User.objects.get(id=request.user.id)
        if user.userBalance < total_price:
            raise serializers.ValidationError({"success": False, 
                                               "message":"Saldo insuficiente"})
        if not type == 'method' and not type== 'digitals':
            if(products.actQuantity == 0):
                raise serializers.ValidationError({"error":"No quedan mas productos disponibles"})
            products.actQuantity -= quantity_asked
            if products.actQuantity < 0:
                raise serializers.ValidationError({"error":"Pide mas de lo que hay"})
        user.userBalance -= total_price
        user.save()

        if type == "fisics":
            transact = Transacts.objects.create(productFisic=products,buyers=buyers,total=total_price, **validated_data)
        elif type=="method":
            transact = Transacts.objects.create(methodProduct=products,buyers=buyers,total=total_price, **validated_data)
        elif type == "digitals":
            transact = Transacts.objects.create(productDigit=products, buyers=buyers,total=total_price,status="Aceptado", **validated_data)
        return transact

class TransactsViewAdminSerializer(serializers.ModelSerializer):
    product= serializers.SerializerMethodField()
    buyers = UserNestedSerializer()
    dateTransact = serializers.DateTimeField(format="%d/%m/%Y %I:%M:%S %p")

    
    class Meta:
        model= Transacts
        fields= ('id','dateTransact', 'product', 'quantity_asked','buyers')

    def get_product(self, obj):
        if obj.productDigit:
            return ProductDigitNestedSerializer(obj.productDigit).data
        if obj.productFisic:
            return ProductNestedSerializer(obj.productFisic).data
        else:
            return None
        
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['total'] = float(result['product']['price']) * float(result['quantity_asked']) 
        return result

class ReportSerializer(serializers.ModelSerializer):
    transact = TransactsSerializer(required=False)
    rMessage = serializers.CharField(error_messages={'required':'Debe especificar las razones de su reporte'})
    dateReport = serializers.DateTimeField(format=dateFormat, read_only=True)
    noReporte =serializers.CharField(required=False)


    class Meta:
        model = ReportTransacts
        fields= ['id','transact','rMessage','dateReport', 'status','noReporte']

    def create(self, validated_data):
        idTransact= self.context.get('idTransact',None)
        request = self.context.get('request',None)
        if idTransact:
            transact= Transacts.objects.filter(id=idTransact).first()

        if transact:
            user = User.objects.get(id=request.user.id)
            noR = uti.generate_invitation_code(5)
            report = ReportTransacts.objects.create(user=user, transact=transact, noReporte=noR, **validated_data)
            return report
        else:
            raise serializers.ValidationError({'error':'No existe'})

class ResetPassSerializer(serializers.Serializer):
    email= serializers.CharField()
    oldPassword= serializers.CharField(style={'input_type':'password'})
    newPassword= serializers.CharField(style={'input_type':'password'})
    retPassword= serializers.CharField(style={'input_type':'password'})

    def validate(self, data):
        email = data.get('email')
        oldPassword = data.get('oldPassword')
        user = authenticate(
            request= self.context.get('request'),
            email=email,
            password = oldPassword
        )  
        if not user:
            raise serializers.ValidationError('Sus credenciales han sido incorrectas', code=401)
        data['user'] = user 
        return data
        
    def update(self,instance, validated_data):
        newPassword = validated_data.get('newPassword','')
        retPassword = validated_data.get('retPassword','')
        if newPassword == '':
            print(newPassword,2)
            raise serializers.ValidationError({'newPassword':['Ingrese un valor valido']})
        if not newPassword == retPassword:
            print(retPassword)
            raise serializers.ValidationError(
                {'newPassword':['Las contraseñas no coinciden'],
                'retPassword':['Las contraseñas no coinciden']}) 
           
        instance.password = make_password(retPassword)
        instance.save()
        return instance 

class AuthenticationSerializer(serializers.Serializer):
    email= serializers.EmailField()
    password = serializers.CharField(style={'input_type':'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request= self.context.get('request'),
            email=email,
            password = password
        )  

        if not user:
            raise serializers.ValidationError('Sus credenciales han sido incorrectas', code=401)

        data['user'] = user 
        return data



    

