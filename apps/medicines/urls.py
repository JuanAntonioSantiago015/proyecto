# URL
from django.urls import path, include

# VIEWS
from . import views

#API
from apps.medicines.api import routers

urlpatterns = [
    
]

urlpatterns+= routers.urlpatterns