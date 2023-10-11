
# API
from rest_framework import serializers

# MODELO
from .models import Medicamento, HistorialMedicamento

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class HistorialMedicamentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialMedicamento
        fields = '__all__'