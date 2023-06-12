from django.contrib import admin
from .models import ProductFisic, ProductDigit, Category,Transacts, User, InvitationCodes, RoleRequests, SubCategory, Stores
 
# Register your models here.
admin.site.register(ProductFisic)
admin.site.register(Category)
admin.site.register(Transacts)
admin.site.register(User)
admin.site.register(InvitationCodes)
admin.site.register(RoleRequests)
admin.site.register(SubCategory)
admin.site.register(ProductDigit)
admin.site.register(Stores)