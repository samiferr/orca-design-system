"""Minimal project that serves the ORCA catalogue: `python demo/manage.py runserver`."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = "orca-demo-only-not-secret"
DEBUG = True
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = ["django.contrib.staticfiles", "django.contrib.humanize", "orca"]
ROOT_URLCONF = "demo.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": ["django.template.context_processors.request"]},
}]
DATABASES = {}
STATIC_URL = "/static/"
USE_TZ = True
TIME_ZONE = "Europe/Paris"

ORCA = {
    "BRAND": {"name": "ORCA"},
    "THEME": "auto",
}
