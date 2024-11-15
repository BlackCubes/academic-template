from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*43osc&ua67am16=(5__f_43@+)4q&3(tu05$ix@)d+ug#--*a"


ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_METHODS = [
    "GET",
]

try:
    from .local import *
except ImportError:
    pass
