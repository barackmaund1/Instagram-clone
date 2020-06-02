from django.apps import AppConfig


class IstaConfig(AppConfig):
    name = 'ista'
    def ready(self):
        import users.signals
