from django.apps import AppConfig


class CacheredisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cacheredis'

    def ready(self):
        import cacheredis.signals
