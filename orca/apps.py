from django.apps import AppConfig


class OrcaConfig(AppConfig):
    name = "orca"
    verbose_name = "ORCA design system"
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        from . import checks  # noqa: F401  (registers the system checks)
