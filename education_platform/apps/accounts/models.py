from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class User(AbstractUser):
    email: models.EmailField = models.EmailField(
        unique=True,
        help_text="Email обязателен для заполнения.",
    )
    username: models.CharField = models.CharField(
        max_length=20,
        unique=True,
        help_text="Имя пользователя обязательно для заполнения.",
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9_]+$",
                message="Имя пользователя может содержать только латинские буквы, цифры и _.",
                code="invalid_username",
            ),
            MinLengthValidator(
                4, "Имя пользователя должно содержать минимум 4 символа."
            ),
        ],
        error_messages={
            "unique": "Пользователь с таким именем пользователя уже существует.",
            "min_length": "Имя пользователя должно содержать минимум 4 символа.",
            "max_length": "Имя пользователя не может превышать 20 символов.",
        },
    )
