# URL
from django.urls import path, include

# VIEWS
from . import views

#API
from apps.medicines.api import routers

app_name = 'medicines'

urlpatterns = [
    path('',views.index,name='index')
]

urlpatterns+= routers.urlpatterns