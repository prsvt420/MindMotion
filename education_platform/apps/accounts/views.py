from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from education_platform.apps.accounts.forms import SignInForm, SignUpForm
from education_platform.apps.accounts.mixins import AnonymousRequiredMixin


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


class SignUpView(AnonymousRequiredMixin, CreateView):
    """Представление для регистрации нового пользователя."""

    form_class: type[SignUpForm] = SignUpForm
    template_name: str = "accounts/signup.html"
    success_url: str = reverse_lazy("info:about_project")

    def form_valid(self, form: SignUpForm) -> HttpResponse:
        response: HttpResponse = super().form_valid(form)
        user = form.instance
        login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")
        return response
