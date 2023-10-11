from django.shortcuts import render

# API
from rest_framework import viewsets

# SERIALIZERS
from .serializer import MedicamentoSerializer

# MODEL
from .models import Medicamento

# Create your views here.
class MedicamentoViewSet(viewsets.ModelViewSet):
    
    serializer_class = MedicamentoSerializer
    queryset = Medicamento.objects.all()