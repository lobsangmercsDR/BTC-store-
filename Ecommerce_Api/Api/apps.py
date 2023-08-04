from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'

    def ready(self):
        from .models import Transacts, ProductFisic,ProductDigit
        from .groups import create_groups
        create_groups()

        # for i in range(0,4):
        #     newObjet = ProductDigit.objects.get(id=1)
        #     newObjet.id= None
        #     newObjet.save()
        # for i in range(20):
        #     newRecord= Transacts(productDigit_id=i+1, quantity_asked=1)
        #     newRecord.save()
