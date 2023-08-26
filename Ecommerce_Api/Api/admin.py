from django.contrib import admin
from .models import ProductFisic,ReportTransacts,GenData,TransactCategories,Deposits,Withdrawals,ProductDigit, Category,Transacts, User,CheckerSolic, InvitationCodes, SubCategory, Stores, MethodProducts
 
# Register your models here.
admin.site.register(TransactCategories)
admin.site.register(ProductFisic)
admin.site.register(Deposits)
admin.site.register(CheckerSolic)
admin.site.register(Category)
admin.site.register(Transacts)
admin.site.register(User)
admin.site.register(InvitationCodes)
admin.site.register(ReportTransacts)
admin.site.register(SubCategory)
admin.site.register(ProductDigit)
admin.site.register(Stores)
admin.site.register(MethodProducts)
admin.site.register(Withdrawals)
admin.site.register(GenData)