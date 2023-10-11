# API
from rest_framework import serializers

# MODELS
from ..models import HistorialTransaccion,DetalleTransaccion

class HistorialTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialTransaccion
        fields = '__all__'

class DetalleTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleTransaccion
        fields = '__all__'