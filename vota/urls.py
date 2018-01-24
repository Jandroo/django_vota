from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('vota/', include('vota.urls')),
    path('admin/', admin.site.urls),
]