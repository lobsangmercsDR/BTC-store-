from django.contrib import admin
from .models import ProductFisic, Category,Transacts, User, InvitationCodes, RoleRequests, SubCategory
 
# Register your models here.
admin.site.register(ProductFisic)
admin.site.register(Category)
admin.site.register(Transacts)
admin.site.register(User)
admin.site.register(InvitationCodes)
admin.site.register(RoleRequests)
admin.site.register(SubCategory)