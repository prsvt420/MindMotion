from typing import Any, List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns: List[Any] = [
    path("admin/", admin.site.urls),
    path(
        "info/",
        include("education_platform.apps.info.urls", namespace="info"),
        name="info",
    ),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
