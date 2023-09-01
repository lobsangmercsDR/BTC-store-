from django.contrib.auth.backends import BaseBackend
from datetime import datetime
import pytz
from .utils import services as uti
from django.contrib.auth.hashers import make_password
from .models import User,InvitationCodes
from django.conf import settings
from django.contrib.auth.backends import ModelBackend

current_timezone = pytz.timezone(settings.TIME_ZONE)

class CustomBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, *args, **kwargss):
        UserModel = User
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                current_time = datetime.now(current_timezone)
                transactsCount =  user.purchases_count()
                if user.last_login != None and transactsCount >= 10:
                    lastAuthDiference =   current_time - user.last_login
                    thereISInvCode = True if InvitationCodes.objects.filter(created_by=user).exists() else False
                    if lastAuthDiference.days < 7 and thereISInvCode == False:
                        CodeInvitation = InvitationCodes(invitationCodes=uti.generate_invitation_code(), description=f"Codigo creado por usuario {user.groups.values_list('name', flat=True).first()}", created_by=user)
                        CodeInvitation.save()
                        print("sssss")
                user.last_login = current_time
                user.save()
                return user
        except UserModel.DoesNotExist:
            return None




class CustomAuthBackend(ModelBackend):

    def check_password(self, password, encoded):
        return super().check_password(password, encoded)

