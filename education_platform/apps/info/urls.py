from typing import List

from django.urls import URLPattern, path

from . import views

app_name: str = "info"

urlpatterns: List[URLPattern] = [
    path("about_project/", views.AboutProjectView.as_view(), name="about_project"),
]
