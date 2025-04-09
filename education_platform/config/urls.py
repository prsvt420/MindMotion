from typing import Any, List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns: List[Any] = [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
