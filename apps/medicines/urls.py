# URL
from django.urls import path, include

# API
from rest_framework import routers


# VIEWS
from . import views

# API ROUTERS
router = routers.DefaultRouter()
router.register(r'medicamentos', views.MedicamentoViewSet,'medicamentos')
router.register(r'historial-medicamento',views.HistorialMedicamentoViewSet,'historial-medicamento')

urlpatterns = [
    path('api/', include(router.urls)),    
]
