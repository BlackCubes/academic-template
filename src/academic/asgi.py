"""
ASGI config for academic project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.conf import settings
from django.core.asgi import get_asgi_application

DJANGO_SETTINGS_MODULE = (
    "academic.settings.dev" if settings.DEBUG else "academic.settings.prod"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)


application = get_asgi_application()
