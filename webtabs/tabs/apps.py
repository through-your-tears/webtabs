from django.apps import AppConfig


class TabsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tabs'

    def ready(self):
        from . import signals
