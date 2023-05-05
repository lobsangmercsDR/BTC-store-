from django.contrib import admin
from .models import Product, Category,Transacts, User, InvitationCodes, RoleRequests
 
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Transacts)
admin.site.register(User)
admin.site.register(InvitationCodes)
admin.site.register(RoleRequests)