# URL
from django.urls import path, include

# API
from rest_framework import routers

# VIEWS
from . import views

# API ROUTERS
router = routers.DefaultRouter()
router.register(r'proveedor', views.ProveedorViewSet, 'proveedor')

urlpatterns = [
    path('api/', include(router.urls))
]
