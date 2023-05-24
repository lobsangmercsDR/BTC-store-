from django.forms import ValidationError

from rest_framework import serializers,exceptions
from .models import Category, Product,Transacts,User,InvitationCodes,RoleRequests
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from .utils import services as uti
import random
import string

dateFormat = serializers.DateTimeField(format="%d/%m/%Y %I:%M:%S %p",required=False)

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
        fields = ['id','email','password','name','createdAt','is_active','group', 'last_login', 'shares_count', 'purchases_count']
        ref_name = 'UserSerializer'

    def get_shares_count(self, obj):
        return obj.shares_count

    def get_purchases_count(self, obj):
        return obj.purchases_count

 
    def get_group(self, obj):
        if obj.is_superuser:
            return "SuperUser"
        elif obj.is_active== False:
            return False
        else:  
            return list(obj.groups.values_list('name',flat=True))[0]


    
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
        print(validated_data)
        if invitation_code:
            invitationObj = InvitationCodes.objects.get(invitationCodes=invitation_code)
            invitationObj.countUsers += 1
            invitationObj.save()
            countUsed = invitationObj.countUsers  
            countcreate= countUsed+1

        group = Group.objects.get(name=group_name[0]) 
        user = User.objects.create_user(**validated_data)
        user.groups.add(group)
        return user

    def update(self, instance,validated_data):
        validated_data = self.context['request'].data   
        group_name = validated_data.pop('add_group', False)
        delete_group = validated_data.pop('delete_group', False)
        
        print(group_name)
        evidence= True if "is_active" in validated_data.keys() or "group" in validated_data.keys() or "group_name" in validated_data.keys()  or "password" in validated_data.keys() else False
        roles = True if self.context.get('roles') == 'true' else False
        if not roles and evidence:
            print(roles)
            print(evidence)
            raise serializers.ValidationError({"message":"Acceso a estas propiedades no tienes"})

        not_found_groups = []
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


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category 
        fields =  ['id','nameCategory','product_count','products']

    def get_product_count(self,obj):
        count = obj.products_quantity
        self.prop = count
        return count
    
    def get_products(self, obj):
        if obj.products_quantity == 0:
            products = "N/A"
            return products
        products = Product.objects.filter(category_id=obj.id, active=True)
        return ProductSerializer(products, many=True).data


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
    category_id = serializers.IntegerField(required=True, write_only=True)
    price = serializers.SerializerMethodField()
    priceProduct = serializers.DecimalField(max_digits=10,decimal_places=2,write_only=True)

    def get_price(self, obj):
        print(obj.priceProduct)
        return f"{obj.priceProduct} USD"

    class Meta:
        model = Product
        fields = [
                    'id',
                    'nameProduct',
                    'price',
                    'dateReleased',
                    'is_digital',
                    'active',
                    'seller', 
                    'category',
                    'category_id',
                    'priceProduct'
                ]


    def create(self, validated_data):
        request = self.context.get('request')
        category_id = validated_data.pop('category_id', None)
        price = validated_data.pop('priceProduct', None)
        validated_data.pop('seller_id')
        print("asdas")
        seller = User.objects.get(id=request.user.id)
        try:
            category = Category.objects.get(id=category_id)
        except:
            raise exceptions.ValidationError("La categoria especificada no existe")
        product = Product.objects.create(seller=seller, priceProduct=price, category=category, **validated_data)
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
            print(valid_fields)
            print(input_fields)
            
            if 'id' in data:
                raise serializers.ValidationError({"Parametro no autorizado":['id']})

            if userValidation['IsSeller'] and not userValidation['IsChecker'] and not userValidation['IsAdmin'] and 'active' in input_fields:
                raise serializers.ValidationError({'message': 'No es checker'})
            
            if not input_fields.issubset(valid_fields):
                invalid_fields = input_fields - valid_fields
                INVList = list(invalid_fields)
                print(INVList)
                raise serializers.ValidationError({"Parametros Invalidos":INVList})
            return super().to_internal_value(data)

class TransactProductNestedSerializer(serializers.ModelSerializer):
    seller = UserNestedSerializer(source='seller_id')

    class Meta:
        model = Product
        fields = ['id','nameProduct','priceProduct','dateReleased','active', 'seller']

class TransactsSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    product = TransactProductNestedSerializer(read_only=True)
    buyers = UserNestedSerializer(read_only=True)
    dateTransact = serializers.DateTimeField(format="%m/%d/%Y %I:%M:%S %p", read_only=True)
    
    class Meta:
        model  = Transacts 
        fields = ['id','dateTransact','product','buyers', 'product_id']

    def create(self, validated_data):
        print(validated_data)
        product_id = validated_data.pop('product_id', None)
        request = self.context.get('request')
        buyer_id= request.user.id
        buyers = User.objects.get(id=buyer_id)
        print(buyers)
        products = Product.objects.get(id=product_id)
        transact = Transacts.objects.create(product=products,buyers=buyers, **validated_data)
        return transact

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



    

