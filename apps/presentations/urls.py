# URL
from django.urls import path, include

# API
from rest_framework import routers

# VIEWS
from . import views

# API - ROUTER
router = routers.DefaultRouter()
router.register(r'presentacion',views.PresentacionviewSet,'presentacion')

urlpatterns = [
    path('api/',include(router.urls))
]
