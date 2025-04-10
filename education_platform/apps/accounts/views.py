from django.contrib.auth import logout
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View


class SignOutView(View):
    """Представление для выхода из аккаунта."""

    @staticmethod
    def get(request: WSGIRequest) -> HttpResponse:
        logout(request)
        return redirect("info:about_project")
