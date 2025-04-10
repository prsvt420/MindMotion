from typing import List

from django.urls import URLPattern, path

from . import views

app_name: str = "accounts"

urlpatterns: List[URLPattern] = [
    path("signout/", views.SignOutView.as_view(), name="signout"),
]
