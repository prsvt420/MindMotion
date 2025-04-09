from typing import Any, List

from django.contrib import admin
from django.urls import path

urlpatterns: List[Any] = [
    path("admin/", admin.site.urls),
]
