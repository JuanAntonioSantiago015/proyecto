# URL
from django.urls import path, include

# VIEWS
from . import views

#API
from apps.medicines.api import routers

app_name = 'medicines'

urlpatterns = [
    path('',views.index,name='index'),
    path('existence/',views.existence,name='existencia'),
    path('defeated/',views.defeated, name='vencidos')
]

urlpatterns+= routers.urlpatterns