# API
from rest_framework import serializers

# MODELS
from .models import UsoTerapeutico, FormaAdministracion, Clasificacion

class UsoTerapeuticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsoTerapeutico
        fields = '__all__'

class FormaAdministracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaAdministracion
        fields = '__all__'

class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = '__all__'