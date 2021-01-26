
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^", include("users.urls")),
    url(r"^admin/", admin.site.urls),
]
