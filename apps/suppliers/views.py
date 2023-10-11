# URL
from django.shortcuts import render

# API
from rest_framework import viewsets

# SERIALIZER
from .serializer import ProveedorSerializer

# MODELS
from .models import Proveedor

# Create your views here.
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer