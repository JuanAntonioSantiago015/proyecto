# API
from rest_framework import serializers

# MODELS
from apps.classifications.models import UsoTerapeutico, FormaAdministracion, Clasificacion

# SERIALIZER
from apps.medicines.api.serializer import MedicamentoSerializer

class UsoTerapeuticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsoTerapeutico
        fields = '__all__'

class FormaAdministracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaAdministracion
        fields = '__all__'

class ClasificacionSerializer(serializers.ModelSerializer):
    medicine_id = serializers.StringRelatedField()
    therepeuticuse_id = serializers.StringRelatedField()
    formadministration_id = serializers.StringRelatedField()
    
    class Meta:
        model = Clasificacion
        fields = '__all__'