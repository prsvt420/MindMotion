from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class SignInForm(AuthenticationForm):
    """Форма для входа в аккаунт."""

    class Meta:
        model = get_user_model()
        fields: tuple = ("username", "password")
