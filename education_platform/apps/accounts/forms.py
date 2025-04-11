from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class SignInForm(AuthenticationForm):
    """Форма для входа в аккаунт."""

    class Meta:
        model = get_user_model()
        fields: tuple = ("username", "password")


class SignUpForm(UserCreationForm):
    """Форма для регистрации нового пользователя."""

    first_name: forms.CharField = forms.CharField(
        required=True,
        error_messages={
            "required": "Имя обязательно для заполнения.",
        },
        label="Имя",
    )
    last_name: forms.CharField = forms.CharField(
        required=True,
        error_messages={
            "required": "Фамилия обязательна для заполнения.",
        },
        label="Фамилия",
    )
    email: forms.EmailField = forms.EmailField(
        required=True,
        error_messages={
            "required": "Email обязателен для заполнения.",
            "invalid": "Некорректный email, попробуйте еще раз.",
            "unique": "Пользователь с таким email уже существует.",
        },
        label="Email",
    )
    username: forms.CharField = forms.CharField(
        required=True,
        error_messages={
            "required": "Имя пользователя обязательно для заполнения.",
            "unique": "Пользователь с таким именем пользователя уже существует.",
        },
        label="Имя пользователя",
    )
    password1: forms.CharField = forms.CharField(
        required=True,
        error_messages={
            "required": "Пароль обязателен для заполнения.",
            "invalid": "Некорректный пароль, попробуйте еще раз.",
        },
        label="Пароль",
    )
    password2: forms.CharField = forms.CharField(
        required=True,
        error_messages={
            "required": "Подтверждение пароля обязательно для заполнения.",
            "invalid": "Пароли не совпадают, попробуйте еще раз.",
        },
        label="Подтверждение пароля",
    )

    class Meta:
        model = get_user_model()
        fields: tuple = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )
