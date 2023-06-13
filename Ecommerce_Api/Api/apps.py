from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'

    def ready(self):
        from .models import ProductDigit
        from .groups import create_groups
        create_groups()

        # for i in range(20):
        #     newRecord= ProductDigit(name=f"Producto en BD {i}", price="2000", subCategory_id=11, text_preview="si",quantity=5,store_id=1)
        #     newRecord.save()
