# URL
from django.shortcuts import render

# API
from rest_framework import viewsets

# SERIALIZERS
from .serializer import SeccionSerializer, UbicacionSerializer, HistorialInvetarioSerializer

# MODELS
from .models import Seccion, Ubicacion, HistorialInvetario

# Create your views here.

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer

class HistorialInventarioViewSet(viewsets.ModelViewSet):
    queryset = HistorialInvetario.objects.all()
    serializer_class = HistorialInvetarioSerializer
