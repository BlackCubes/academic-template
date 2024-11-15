import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application

DJANGO_SETTINGS_MODULE = (
    "academic.settings.dev" if settings.DEBUG else "academic.settings.prod"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

application = get_wsgi_application()
