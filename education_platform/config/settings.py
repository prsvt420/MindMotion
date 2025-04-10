import os
from pathlib import Path
from typing import Any, Dict, List, Optional

BASE_DIR: Path = Path(__file__).resolve().parent.parent

SECRET_KEY: Optional[str] = os.getenv("DJANGO_SECRET_KEY")

DEBUG: bool = os.getenv("DJANGO_DEBUG") == "True"

ALLOWED_HOSTS: List[str] = [
    "127.0.0.1",
    #  server_ip
    #  domain.*
    #  www.domain.*
]

INTERNAL_IPS: List[str] = [
    "127.0.0.1",
]

INSTALLED_APPS: List[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "csp",
    "education_platform.apps.info",
    "education_platform.apps.accounts",
    "education_platform.apps.catalog",
    "education_platform.apps.core",
]

MIDDLEWARE: List[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF: str = "config.urls"

TEMPLATES: List[Dict[str, Any]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION: str = "config.wsgi.application"

DATABASES: Dict[str, Any] = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DJANGO_POSTGRES_DB"),
        "USER": os.getenv("DJANGO_POSTGRES_USER"),
        "PASSWORD": os.getenv("DJANGO_POSTGRES_PASSWORD"),
        "HOST": "localhost" if DEBUG else os.getenv("DJANGO_POSTGRES_HOST"),
        "PORT": os.getenv("DJANGO_POSTGRES_PORT", default=5432),
    }
}

AUTH_PASSWORD_VALIDATORS: List[Dict[str, str]] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "education_platform.apps.accounts.custom_validators.CustomMinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE: str = "ru-RU"

TIME_ZONE: str = "Europe/Moscow"

USE_I18N: bool = True

USE_TZ: bool = True

STATIC_URL: str = "static/"
STATICFILES_DIRS: List[Any] = [
    BASE_DIR / "static",
]
STATIC_ROOT: Path = BASE_DIR / "staticfiles"

MEDIA_URL: str = "media/"
MEDIA_ROOT: Path = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

FIXTURE_DIRS: List[str] = [
    "fixtures",
]

CONTENT_SECURITY_POLICY: Dict[str, Any] = {
    "DIRECTIVES": {
        "default-src": ["'self'"],
        "font-src": ["'self'", "https://fonts.gstatic.com"],
        "img-src": ["'self'"],
        "script-src": ["'self'"],
        "style-src": ["'self'", "https://fonts.googleapis.com/", "'unsafe-inline'"],
        "worker-src": ["'self'", "blob:"],
    }
}

AUTHENTICATION_BACKENDS: List[str] = [
    "education_platform.apps.accounts.authentication_backends.EmailAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL: str = "accounts.User"
