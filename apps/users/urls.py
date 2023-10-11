# URL
from django.urls import path, include

# API - ROUTERS
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required



# API ROUTERS
router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('docs/', include_docs_urls(title='USUARIOS API')),
    
]
