import random
import string
from rest_framework import exceptions
from .authentications import IsAdmin, IsSeller, IsChecker, IsBuyer, IsGroupAccepted

class services:
    def generate_invitation_code(length=15):
        """Genera un codigo de invitacion aleatorio."""
        letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    def hasOrNotPermission(clss, request, view,obj=None,authClass=None, oneObj=False):
        userComp={}
        if authClass != None:
            if oneObj== False:
                for item in authClass:
                    userComp[item.__name__] = True if item.has_permission(clss, request, view) else False
            else:
                for item in authClass:
                    userComp[item.__name__] = True if item.has_object_permission(clss, request, view,obj) else False
        return userComp
    

    def checkAuth(request, raise_exception=False):
        print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            if raise_exception:
                raise exceptions.AuthenticationFailed("No está authenticado")
            else:
                return False
        return True
    
    def checkAdminSeller(request, raise_exception=True):
        groups_queryset = request.user.groups.all()
        listGroups = []
        for group in groups_queryset:
            listGroups.append(group.name)
        if not 'sellers' in listGroups and not'administrator' in listGroups:
            raise exceptions.PermissionDenied("No tienes permiso para esta vista")
        return listGroups

