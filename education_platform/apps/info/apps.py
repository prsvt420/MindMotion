from django.apps import AppConfig


class InfoConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "education_platform.apps.info"
    verbose_name: str = "Info"
    label: str = "info"
