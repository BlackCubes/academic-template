from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views import debug

urlpatterns = [path("admin/", admin.site.urls), path("", debug.default_urlconf)]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
