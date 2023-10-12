
# API
from rest_framework import serializers

# MODELO
from apps.medicines.models import Medicamento, HistorialMedicamento

# SERIALIZER
from apps.suppliers.api.serializer import ProveedorSerializer
from apps.presentations.api.serializer import PresentacionSerializer

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'


class HistorialMedicamentorSerializer(serializers.ModelSerializer):
    medicine_id = serializers.StringRelatedField()
    supplier_id = serializers.StringRelatedField()
    presentation_id = serializers.StringRelatedField()
    class Meta:
        model = HistorialMedicamento
        fields = '__all__'