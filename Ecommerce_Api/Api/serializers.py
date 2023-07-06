from django.forms import ValidationError

from rest_framework import serializers,exceptions
from .models import Category, ProductFisic, ProductDigit,ReportTransacts, Withdrawals, TransactCategories, CheckerSolic, Transacts,MethodProducts,User,InvitationCodes,RoleRequests, SubCategory, Stores
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from .utils import services as uti
import random
import requests as rq
import string

dateFormat = "%d/%m/%Y %I:%M:%S %p"

class StoreSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Stores
        fields = ['id', 'nameStore','seller','product_count']
    
    def get_product_count(self, obj):
        count = obj.product_count 


class ProductDigitSerializer(serializers.ModelSerializer):
    dateCreated = serializers.DateTimeField(format="%d/%m/%Y %I:%M %p")

    class Meta:
        model = ProductDigit
        fields = ['id', 'name', 'price','no_solicitud', 'description','comisionCheck','additional_details','needChecker','orgQuantity','actQuantity', 'dateCreated','store_id']



    def to_representation(self, instance):
        try:
            product = ProductDigit.objects.filter(id=instance['id']).first()
            store = Stores.objects.get(id=instance['store_id'])
            serializer = StoreSerializer(store)
            instance['store_id'] = serializer.data
            result=super().to_representation(instance)
            result['no_solicitudes'] = product.solic_count 
            return result
        except:
            store = Stores.objects.get(id=instance.store_id)
            product = ProductDigit.objects.filter(id=instance.id).first()
            serializer = StoreSerializer(store)
            result = super().to_representation(instance)
            result['store_id'] = serializer.data
            result['no_solicitudes'] = product.solic_count
            return result
            






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
    shares_count = serializers.SerializerMethodField()
    purchases_count = serializers.SerializerMethodField()
    
    class Meta:
        model = get_user_model() 
        extra_kwargs = {'password':{'write_only':True}}
        fields = ['id','email','password','name','userBalance','phoneNumber','direction','wallet_address','createdAt','is_active','group', 'last_login', 'shares_count', 'purchases_count']
        ref_name = 'UserSerializer'

    def get_shares_count(self, obj):
        return obj.shares_count

    def get_purchases_count(self, obj):
        return obj.purchases_count

 
    def get_group(self, obj):
        print(obj.groups, "59")
        if obj.is_superuser:
            return "SuperUser"
        elif obj.is_active== False:
            return False
        else:  
            return list(obj.groups.values_list('name',flat=True))[0]

class WithDrawSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)


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
    store = StoreSerializer()
    transacts_count = serializers.SerializerMethodField()

    class Meta:
        model = MethodProducts
        fields = ['id','nameProduct', 'dateCreated','actQuantity','quantity','sendDirection','description','price','store','image','transacts_count']


    def get_transacts_count(self, obj):
        return obj.transacts_count


class UserCreatorSerializer(serializers.ModelSerializer):
    add_group = serializers.CharField(read_only=True)
    delete_group= serializers.CharField(read_only=True)
    invitation_code = serializers.CharField()
    name = serializers.CharField(required=True)
    confirm_pass = serializers.CharField(write_only=True)

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
        fields = ['id','email','password','confirm_pass','name','is_active','add_group', 'invitation_code', 'delete_group']
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
        "api_key": "7c5a-c48b-9afb-7799",
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
        
        print(group_name)
        evidence= True if "is_active" in validated_data.keys() or "group" in validated_data.keys() or "group_name" in validated_data.keys()  or "password" in validated_data.keys() else False
        roles = True if self.context.get('roles') == 'true' else False
        if not roles and evidence:
            print(roles)
            print(evidence)
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
        return super().update(instance, validated_data)
            

class RoleRequestsSerializer(serializers.ModelSerializer):
    user = UserNestedSerializer(read_only=True)
    class Meta:
        model =RoleRequests
        fields = ['id', 'is_role','is_password','message','user','approved']
        write_only_fields = ['is_role','is_password']
        ref_name = 'UserSerializer'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        listT = []
        if data['is_role']:
            listT.append('Role Change')
        if data['is_password']:
            listT.append('Password Change')
        data['type'] = listT
        return data

    
    def create(self, validated_data):
        
        role = validated_data.get('is_role')
        password = validated_data.get('is_password')
        listTypes = []
        if not role and not password:
            raise serializers.ValidationError({'message':'Debe especificar un tipo valido'})
        user=User.objects.get(id=self.context.get('request').user.id)
        roleRequest = RoleRequests.objects.create(user=user, **validated_data)
        return roleRequest

class SubCategorySerializer(serializers.ModelSerializer):
    purchased = serializers.SerializerMethodField()

    
    class Meta:
        model = SubCategory
        fields = ['id', 'nameSubCategory','priceSubCategory', 'purchased','minPriceBTC','maxPriceBTC']

    def get_purchased(self, obj):
        idUser = self.context['request'].user.id
        print(idUser)
        hasPurchased = TransactCategories.objects.filter(user_id=idUser, subCategory=obj.id).exists()
        print(hasPurchased)
        if hasPurchased:
            return True
        else:
            return False

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
    price = serializers.SerializerMethodField()
    priceProduct = serializers.DecimalField(max_digits=10,decimal_places=2,write_only=True)
    image_product = serializers.ImageField(required=False)
    subCategory = serializers.SerializerMethodField()

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
                    'nameProduct',
                    'price',
                    'image_product',
                    'dateReleased',
                    'active',
                    'actQuantity',
                    'brand',
                    'aditional_details',
                    'seller', 
                    'variants',
                    'quantity',
                    'address_direction',
                    'description',
                    'category',
                    'subCategory',
                    'aditional_details',
                    'priceProduct'
                ]


    # def validate_description(self, value):
    #     print(value,22)
    #     if value=='':
    #         raise serializers.ValidationError("Debe ingresar una descripcion valida del producto")
    #     return value

    def validate_subCategory(self, value):
        print(value, 31)
        if value == 0: 
            raise serializers.ValidationError("No se proporcionó ninguna subcategoría")
        subObj = SubCategory.objects.filter(id=value).first()
        print(len(subObj))
        if len(subObj) == 0:
            print("test")
            raise serializers.ValidationError("La sub categoria planteada no existe")
        return value

    def validate_quantity(self, value): 
        if value==0:
            raise serializers.ValidationError("El numero no puede ser 0")
        return value
    
    def validate_priceProduct(self, value):
        if value==0:
            raise serializers.ValidationError("Ingrese un valor valido")
        return value

    

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data = request.data
        category_id = validated_data.pop('subCategory', None)
        print(category_id, 222)
        price = validated_data.pop('priceProduct', None)
        seller = User.objects.get(id=request.user.id)
        subCategory = SubCategory.objects.get(id=category_id)
        product = Product.objects.create(seller=seller, priceProduct=price, subCategory=subCategory, **validated_data)
        return product

    def update(self, instance, validated_data):
        userValidation= self.context.get('userPermision')
        if userValidation['IsChecker'] and not userValidation['IsAdmin'] and any( key != 'active' for key in validated_data.keys()):
            raise serializers.ValidationError({"message":"No puede editar esto"}) 
        return super().update(instance, validated_data)

    def to_internal_value(self, data):
            valid_fields = set(self.fields.keys())
            input_fields = set(data.keys())
            userValidation= self.context.get('userPermision') 
            
            if 'id' in data:
                raise serializers.ValidationError({"Parametro no autorizado":['id']})

            if userValidation['IsSeller'] and not userValidation['IsChecker'] and not userValidation['IsAdmin'] and 'active' in input_fields:
                raise serializers.ValidationError({'message': 'No es checker'})
            
            if not input_fields.issubset(valid_fields):
                invalid_fields = input_fields - valid_fields
                INVList = list(invalid_fields)
                raise serializers.ValidationError({"Parametros Invalidos":INVList})
            return super().to_internal_value(data)

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
    
    class Meta:
        model  = Transacts 
        fields = ['id','dateTransact','quantity_asked','status','sendDirection','productDigit','productFisic','buyers', 'productDigit_id', 'sendDirection','noSeguimiento','company']

    def create(self, validated_data):
        print(validated_data)
        type = self.context.get('type') 
        product_id = validated_data.pop('productDigit_id', None)
        print(type)
        if not type == 'method' and not type == 'digitals':
            quantity_asked = validated_data['quantity_asked'] 
        
        request = self.context.get('request')
        buyer_id= request.user.id
        print(buyer_id)
        buyers = User.objects.get(id=buyer_id)
        total_price = 0
        try:
            if type == 'fisics':
                products = ProductFisic.objects.get(id=product_id)
                total_price = quantity_asked * products.priceProduct
            elif type=='method':
                products = MethodProducts.objects.get(id=product_id)
                total_price = products.price
            elif type == 'digitals':
                products = ProductDigit.objects.get(id=product_id)
                total_price = products.price
        except:
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
        products.save() 
        print(products)
        if type == "fisics":
            transact = Transacts.objects.create(productFisic=products,buyers=buyers, **validated_data)
        elif type=="method":
            transact = Transacts.objects.create(methodProduct=products,buyers=buyers, **validated_data)
        elif type == "digitals":
            transact = Transacts.objects.create(productDigit=products, buyers=buyers, **validated_data)
        return transact
    

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



    

