from typing import List

from django.urls import URLPattern, path

from . import views

app_name: str = "info"

urlpatterns: List[URLPattern] = [
    path("about_project/", views.AboutProjectView.as_view(), name="about_project"),
    path("about_team/", views.AboutTeamView.as_view(), name="about_team"),
    path("policy/", views.PolicyView.as_view(), name="policy"),
    path("terms/", views.TermsView.as_view(), name="terms"),
]
