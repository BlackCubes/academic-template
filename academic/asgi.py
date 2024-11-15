import os

from django.core.asgi import get_asgi_application

DJANGO_SETTINGS_MODULE = (
    "academic.settings.dev"
    if (os.getenv("DEBUG", "TRUE") == "TRUE")
    else "academic.settings.prod"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)


application = get_asgi_application()
