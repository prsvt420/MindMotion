from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "education_platform.apps.accounts"
    verbose_name: str = "Accounts"
    label: str = "accounts"
