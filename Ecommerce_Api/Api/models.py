from django.db import models   
from datetime import datetime
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    Group
)
from .utils import services as uti
from django.utils.timezone import now, timedelta 


def generate_file_path(instance,   filename, avatar=False):
    filename = uti.generate_invitation_code(6)

    if type(instance).__name__ == 'ProductFisic':
        return f'images/{filename}.jpg'
    elif type(instance).__name__ == 'Stores':
        if avatar:
            return f'images/store/avt/{filename}.jpg'
        else:
            print(filename)
            return f'images/store/bann/{filename}.jpg'
        

class UserManager(BaseUserManager):
    def create_user(self,email, password, **args):
        if not email:
            raise ValueError('Falta email')
        user = self.model(email=email, **args)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, **args):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user 

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name  = models.CharField(max_length=50)
    wallet_address = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    userBalance = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def total_registered(self, date=None,all=False):
        print(2222)
        if not date:
            date = datetime.now()
        if all ==False:
            user =  User.objects.filter(createdAt__range=(date.date(),date.date() +timedelta(days=1)))
        else:
            user = User.objects.all()
        return user.aggregate(total_reg = models.Count('id'))['total_reg']


    def purchases_count(self):
        return self.transacts_set.count()


class Category(models.Model):
    nameCategory = models.CharField(max_length=50)


class SubCategory(models.Model):
    nameSubCategory = models.CharField(max_length=50)
    minPriceBTC = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    maxPriceBTC = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    priceSubCategory = models.DecimalField(max_digits=10, decimal_places=2)
    userCreator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Withdrawals(models.Model):
    OPTIONS = (
    ('Pendiente','Pendiente'),
    ('Aprobada','Aprobada'),
    ('Rechazada','Rechazada')
    )
    
    no_orden = models.IntegerField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=50,choices=OPTIONS, default="Pendiente")
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_review = models.DateField(default=None, blank=True, null=True)
    walletRequested = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Deposits(models.Model):
    no_orden= models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tasaDepositMoment = models.DecimalField(max_digits=10, decimal_places=2)
    quantityUSD = models.DecimalField(max_digits=10, decimal_places=2)
    status= models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

class Stores(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    avatar_img = models.ImageField(upload_to=lambda instance, filename: generate_file_path(instance, filename, avatar=True), null=True)
    banner_img = models.ImageField(upload_to=generate_file_path, null=True)
    seller = models.OneToOneField(User, on_delete= models.CASCADE)
    

    @property
    def product_count(self):
        return self.productfisic_set.count() + self.productdigit_set.count() + self.methodproducts_set.count()

class MethodProducts(models.Model):
    name = models.CharField(max_length=50)
    dateCreated = models.DateTimeField(auto_now_add=True)
    actQuantity = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    sendDirection = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=generate_file_path)
    
    @property
    def transacts_count(self):
        return self.transacts_set.count()
        
class ProductFisic(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=generate_file_path, default=None)
    description = models.CharField(max_length=200, default="")
    actQuantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dateCreated = models.DateField(auto_now_add=True)
    address_direction = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    brand = models.CharField(max_length=50, default="")
    aditional_details = models.CharField(max_length=200, default="")
    quantity = models.IntegerField(default=0)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)





class ProductDigit(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    dateCreated = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=800)
    aditional_details = models.CharField(max_length=800)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    text_preview = models.CharField(max_length=200)
    needChecker = models.BooleanField(default=True)
    no_solicitud = models.IntegerField(default=0)
    comisionCheck = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    checkerText = models.CharField(max_length=500,blank=True)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)

    @property
    def solic_count(self):
        return self.checkersolic_set.count()




class CheckerSolic(models.Model):
    OPTIONS = (
        ('active','Activo'),
        ('canceled','Invalido'),
        ('pending','Pendiente'),
        ('expired','Expirado')
        )

    product = models.ForeignKey(ProductDigit, on_delete=models.CASCADE)
    dateCreated= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=OPTIONS)


class Transacts(models.Model):
    OPTIONS = (
        ('Entregado','Entregado'),
        ('Procesando','Procesando'),
        ('Aceptado','Aceptado'),
        ('Rechazado','Rechazado')
        )


    dateTransact = models.DateTimeField(auto_now_add=True)
    sendDirection = models.CharField(max_length=50,default="", null=True)
    productFisic = models.ForeignKey(ProductFisic, on_delete=models.SET_NULL, default=None, null=True)
    productDigit = models.ForeignKey(ProductDigit, on_delete=models.SET_NULL, default=None, null=True)
    methodProduct = models.ForeignKey(MethodProducts, on_delete=models.SET_NULL, default=None, null=True)
    quantity_asked = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=50, choices=OPTIONS, default='Procesando')
    buyers = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    company = models.CharField(max_length=50, default="N/A")
    noSeguimiento = models.CharField(max_length=50, default="N/A")

    def total_transacts_amount(self, date=None, all=False):
        if not date:
            date = datetime.now()
        if all ==False:
            transacts =  Transacts.objects.filter(dateTransact__range=(date.date(),date.date() +timedelta(days=1)))
        else:
            transacts  = Transacts.objects.all()
        result = transacts.aggregate(total_amount=models.Sum('total'))['total_amount']
        return 0 if not result else result

    def total_num_shares(self,date=None, all=False):
        if not date:
            date = datetime.now()
        if all ==False:
            transacts =  Transacts.objects.filter(dateTransact__range=(date.date(),date.date() +timedelta(days=1)))
        else:
            transacts = Transacts.objects.all()
        return transacts.aggregate(total_count=models.Count('id'))['total_count']
    
class TransactCategories(models.Model):
    dateTransact = models.DateTimeField(auto_now_add=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ReportTransacts(models.Model):
    OPTIONS = (
        ('En proceso','En proceso'),
        ('Resuelto','Resuelto'),
        ('Rechazado','Rechazado')
        )

    rMessage = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transact =models.ForeignKey(Transacts, on_delete=models.CASCADE)
    dateReport = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=OPTIONS, default='En proceso', max_length=10)
    noReporte = models.CharField(max_length=6)
    

class InvitationCodes(models.Model):
    invitationCodes = models.CharField(max_length=15,default=uti.generate_invitation_code())
    description = models.CharField(max_length=50, blank=True)
    countUsers = models.IntegerField(default=0)
    is_expired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    expire_date = models.DateTimeField(default=now() + timedelta(days=7))

    
    def save(self, *args, **kwargs):
        if self.expire_date < now():
            self.is_expired = True
        super().save(*args, **kwargs)


class GenData(models.Model):
    secret_key= models.CharField(max_length=50)
    price_checker = models.DecimalField(max_digits=10, decimal_places=2)