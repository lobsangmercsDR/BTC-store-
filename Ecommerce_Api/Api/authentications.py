from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class AllowAny(BaseAuthentication):
    def has_permission(self, request,view):
        return True

class IsAdmin(BaseAuthentication):
    def has_permission(self, request,view):
        user =request.user
        print(user.is_superuser,22)
        if user.groups.filter(name="administrator").exists() or user.is_superuser:
            return True
        else:
            return False
    
    def has_object_permission(self, request, view,obj):
        user =request.user
        print(user.is_superuser,2)
        if user.groups.filter(name="administrator").exists() or user.is_superuser:            
            if view.__class__.__name__== 'ProductView':
                print("aja")
                if user.is_superuser:
                    return True
                if 'administrator' in obj.seller.groups.values_list('name',flat=True):
                    if request.user.id == obj.seller.id:
                        return True
                    else:
                        return False
                else:
                    return False
                
            if view.__class__.__name__== 'ProductsDigitView':
                print(11)
                if user.is_superuser:
                    return True
                if 'administrator' in obj.seller.groups.values_list('name',flat=True):
                    if request.user.id == obj.seller.id:
                        return True
                    else:
                        return False
                else:
                    return False
            elif view.__class__.__name__== 'TransactsView':
                if 'administrator' in obj.buyers.groups.values_list('name',flat=True) or obj.buyers.is_superuser:
                    if request.user.id == obj.buyers.id:
                        return True
                    else:
                        return False
                else:
                    return True
            elif view.__class__.__name__=='UserView':
                    print("asasass")
                    print(request.user.is_superuser,"ss")
                    if request.user.is_superuser:
                        print("a")
                        return True
                    if 'administrator' in obj.groups.values_list('name',flat=True) or obj.is_superuser:
                        if request.user.id == obj.id:
                            return True
                        else:
                            return False
                    else:
                        return True
            elif view.__class__.__name__=='InvitationCodeView':
                    if request.user.is_superuser == False:
                        if request.user.id == obj.id:
                            return True
                        else:
                            return False
                    else:
                        return True

        else:
            return False

class IsSeller(BaseAuthentication):
    def has_permission(self, request,view):
        user =request.user
        if user.groups.filter(name="sellers").exists():
            return True
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        if view.__class__.__name__ == "ProductsView":
            if request.user.id == obj.seller_id or request.user.is_superuser==True:
                return True
            else:
                return False

        elif view.__class__.__name__ == "TransactsView":
            if request.user.id == obj.buyers_id or request.user.is_superuser==True:
                return True
            else:
                return False


class IsBuyer(BaseAuthentication):
    def has_permission(self, request,view):
        user =request.user
        if user.groups.filter(name="buyers").exists():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.__class__.__name__ =="TransactsView":
            if request.user.id == obj.buyers_id or request.user.is_superuser==True:
                return True
            else:
                return False
        elif view.__class__.__name__ == "ProductView":
            return False
        elif view.__class__.__name__=='UserView':
            print("Hola")
            if request.user.id == obj.id:
                return True
            else:
                return False

class IsChecker(BaseAuthentication):
    def has_permission(self, request,view):
        user =request.user
        if user.groups.filter(name="checkers").exists():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.__class__.__name__ == "ProductView":
            user =request.user
            if user.groups.filter(name="checkers").exists():
                print("hola")
                print(request.data)
                if not any( key != 'active' for key in request.data.keys()):
                    return True 
        else:
            return False

class IsGroupAccepted(BaseAuthentication):
    def has_permission(self, request, view):
        user =request.user
        isChecker = user.groups.filter(name="checkers").exists()
        isBuyer = user.groups.filter(name="buyers").exists()
        isSeller = user.groups.filter(name="sellers").exists()
        isAdmin = user.groups.filter(name="administrator").exists()

        if isChecker or isBuyer or IsSeller or isAdmin or user.is_superuser:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True

        