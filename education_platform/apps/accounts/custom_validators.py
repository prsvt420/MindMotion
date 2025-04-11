from typing import Optional

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomMinimumLengthValidator:
    """Валидатор минимальной длины пароля."""

    def __init__(self, min_length: int = 8) -> None:
        self.min_length = min_length

    def validate(self, password: str, user: Optional[User] = None) -> None:
        if len(password) < self.min_length:
            raise ValidationError(
                "Ваш пароль должен содержать минимум 8 символов.",
                code="password_too_short",
            )

    def get_help_text(self) -> str:
        return f"Пароль должен содержать минимум {self.min_length} символовa."
