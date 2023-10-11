# URL
from django.shortcuts import render

# API
from rest_framework import viewsets

# SERIALIZER
from .serializer import PresentacionSerializer

# MODELS
from .models import Presentacion

# Create your views here.
class PresentacionviewSet(viewsets.ModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionSerializer
