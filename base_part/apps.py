from django.apps import AppConfig


class BasePartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_part'
