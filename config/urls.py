from django.contrib import admin
from django.urls import path
from . import health

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health.health_check, name='health_check'),
    path('', health.health_check),
]
