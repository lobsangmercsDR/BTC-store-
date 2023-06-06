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
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()


    @property
    def purchases_count(self):
        return self.transacts_set.count()

    @property
    def shares_count(self):
        return self.product_set.count()

class Category(models.Model):
    nameCategory = models.CharField(max_length=50)

class SubCategory(models.Model):
    nameSubCategory = models.CharField(max_length=50)
    minPriceBTC = models.DecimalField(max_digits=10, decimal_places=2)
    maxPriceBTC = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class ProductFisic(models.Model):
    nameProduct = models.CharField(max_length=50)
    image_product = models.ImageField(upload_to='images/', default=None)
    description = models.CharField(max_length=200, default="")
    priceProduct = models.DecimalField(max_digits=10, decimal_places=2)
    dateReleased = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)
    brand = models.CharField(max_length=50, default="")
    aditional_details = models.CharField(max_length=200, default="")
    variants = models.CharField(max_length=200, default="")
    quantity = models.IntegerField(default=0)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

class ProductDigit(models.Model):
    name_PD = models.CharField(max_length=50)
    price_PD = models.DecimalField(max_digits=10,decimal_places=2)
    subCategory_PD = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    text_preview_PD = models.CharField(max_length=200)
    quantity_PD = models.IntegerField(default=0)

class Transacts(models.Model):
    dateTransact = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(ProductFisic, on_delete=models.CASCADE,  default=1)
    buyers = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

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


class RoleRequests(models.Model):
    is_role = models.BooleanField()
    is_password = models.BooleanField()
    message = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)