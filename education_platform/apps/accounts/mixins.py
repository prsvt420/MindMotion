from typing import Dict, Tuple

from django.contrib.auth.mixins import AccessMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect


class AnonymousRequiredMixin(AccessMixin):
    """Миксин для проверки, что пользователь не авторизован."""

    def dispatch(
        self, request: HttpRequest, *args: Tuple, **kwargs: Dict
    ) -> HttpResponse:
        if request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)  # type: ignore

    def handle_no_permission(self) -> HttpResponseRedirect:
        """Перенаправление для авторизованных пользователей."""
        return redirect("info:about_project")
