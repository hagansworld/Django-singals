from django.apps import AppConfig


class SignalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "signals"

    # configure the signals
    def ready(self):
        import signals.signals
