# URL
from django.urls import path, include

# API
from rest_framework import routers

# VIEWS
from . import views

# API ROUTERS
router = routers.DefaultRouter()
router.register(r'historial-transaccion', views.HistorialTransaccionViewSet, 'historial-transaccion')
router.register(r'detalle-transaccion', views.DetalleTransaccionViewSet, 'detalle-transaccion')

urlpatterns = [
    path('api/', include(router.urls))
]