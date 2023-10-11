# URL
from django.shortcuts import render

# API
from rest_framework import viewsets

# SERIALIZER
from .serializer import HistorialTransaccionSerializer, DetalleTransaccionSerializer

# MODELS
from .models import HistorialTransaccion, DetalleTransaccion

# Create your views here.
class HistorialTransaccionViewSet(viewsets.ModelViewSet):
    queryset = HistorialTransaccion.objects.all()
    serializer_class = HistorialTransaccionSerializer

class DetalleTransaccionViewSet(viewsets.ModelViewSet):
    queryset = DetalleTransaccion.objects.all()
    serializer_class = DetalleTransaccionSerializer