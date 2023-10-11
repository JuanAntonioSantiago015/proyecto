from django.shortcuts import render

# API
from rest_framework import viewsets

# SERIALIZERS
from .serializer import MedicamentoSerializer, HistorialMedicamentorSerializer

# MODEL
from .models import Medicamento, HistorialMedicamento

# Create your views here.
class MedicamentoViewSet(viewsets.ModelViewSet):    
    serializer_class = MedicamentoSerializer
    queryset = Medicamento.objects.all()

class HistorialMedicamentoViewSet(viewsets.ModelViewSet):
    queryset = HistorialMedicamento.objects.all()
    serializer_class = HistorialMedicamentorSerializer