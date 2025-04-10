from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View

from education_platform.apps.accounts.forms import SignInForm


class SignOutView(View):
    """Представление для выхода из аккаунта."""

    @staticmethod
    def get(request: WSGIRequest) -> HttpResponse:
        logout(request)
        return redirect("info:about_project")


class SignInView(LoginView):
    """Представление для входа в аккаунт."""

    form_class: type[AuthenticationForm] | None = SignInForm
    template_name: str = "accounts/signin.html"
    redirect_authenticated_user: bool = True

    def get_success_url(self) -> str:
        return reverse_lazy("info:about_project")
