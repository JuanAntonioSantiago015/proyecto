# URL
from django.urls import path, include

# API
from rest_framework import routers

# VIEWS
from . import views

# API - ROUTES
router = routers.DefaultRouter()
router.register(r'historial-inventario',views.HistorialInventarioViewSet,'historial-inventario')
router.register(r'ubicacion', views.UbicacionViewSet, 'ubicacion')
router.register(r'seccion',views.SeccionViewSet,'seccion')


urlpatterns = [
    path('api/',include(router.urls))
]
