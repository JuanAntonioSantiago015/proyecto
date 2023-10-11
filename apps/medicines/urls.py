# URL
from django.urls import path, include

# API
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

# VIEWS
from . import views

router = routers.DefaultRouter()
router.register(r'medicine', views.MedicamentoViewSet,'medicamentos')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='MEDICAMENTOS API')),
]
