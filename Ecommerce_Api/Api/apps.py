from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'

    def ready(self):
        from .models import Transacts
        from .groups import create_groups
        create_groups()

        # for i in range(1,23):
        #     Transacts.objects.create(productDigit_id=i, quantity_asked=1)
        # for i in range(20):
        #     newRecord= Transacts(productDigit_id=i+1, quantity_asked=1)
        #     newRecord.save()
