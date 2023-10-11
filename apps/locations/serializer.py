# API
from rest_framework import serializers

# MODELS
from .models import Ubicacion, Seccion, HistorialInvetario

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

class HistorialInvetarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialInvetario
        fields = '__all__'