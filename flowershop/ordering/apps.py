from django.apps import AppConfig


class OrderingConfig(AppConfig):
    name = 'ordering'


    def ready(self):
        import ordering.signals
