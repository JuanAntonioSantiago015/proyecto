# API
from rest_framework import serializers

# MODELS
from ..models import HistorialTransaccion,DetalleTransaccion

# SERIALIZADOR
from apps.users.api.serializers import UserSerializer
from apps.medicines.api.serializer import MedicamentoSerializer


class HistorialTransaccionSerializer(serializers.ModelSerializer):
    user_id = serializers.StringRelatedField()
    class Meta:
        model = HistorialTransaccion
        fields = '__all__'


class DetalleTransaccionSerializer(serializers.ModelSerializer):
    transaction_id = serializers.StringRelatedField()
    medicine_id = serializers.StringRelatedField()
    class Meta:
        model = DetalleTransaccion
        fields = '__all__'