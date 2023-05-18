from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'

    def ready(self):
        from .groups import create_groups
        create_groups()
