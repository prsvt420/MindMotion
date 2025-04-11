from django.apps import AppConfig


class CourseCatalogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name: str = "education_platform.apps.catalog"
    verbose_name: str = "Catalog"
    label: str = "catalog"
