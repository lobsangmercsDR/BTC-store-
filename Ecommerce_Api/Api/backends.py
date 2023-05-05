from django.contrib.auth.backends import BaseBackend
from datetime import datetime
import pytz
from django.contrib.auth.hashers import make_password
from .models import User
from django.conf import settings
from django.contrib.auth.backends import ModelBackend

current_timezone = pytz.timezone(settings.TIME_ZONE)

class CustomBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, *args, **kwargss):
        UserModel = User
        print(make_password(password))
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                current_time = datetime.now(current_timezone)
                user.last_login = current_time
                user.save()
                return user
        except UserModel.DoesNotExist:
            return None




class CustomAuthBackend(ModelBackend):

    def check_password(self, password, encoded):
        return super().check_password(password, encoded)

