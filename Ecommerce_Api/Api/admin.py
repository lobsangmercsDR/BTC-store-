from django.contrib import admin
from .models import ProductFisic,ReportTransacts,TransactCategories, ProductDigit, Category,Transacts, User,CheckerSolic, InvitationCodes, RoleRequests, SubCategory, Stores, MethodProducts
 
# Register your models here.
admin.site.register(TransactCategories)
admin.site.register(ProductFisic)
admin.site.register(CheckerSolic)
admin.site.register(Category)
admin.site.register(Transacts)
admin.site.register(User)
admin.site.register(InvitationCodes)
admin.site.register(ReportTransacts)
admin.site.register(RoleRequests)
admin.site.register(SubCategory)
admin.site.register(ProductDigit)
admin.site.register(Stores)
admin.site.register(MethodProducts)