# API
from rest_framework import serializers

# MODELS
from apps.locations.models import Ubicacion, Seccion, HistorialInvetario

# SERIALIZER
from apps.medicines.api.serializer import MedicamentoSerializer


class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

class HistorialInvetarioSerializer(serializers.ModelSerializer):

    medicine_id = serializers.StringRelatedField()
    location_id = serializers.StringRelatedField()
    locationsection_id = serializers.StringRelatedField()
    
    class Meta:
        model = HistorialInvetario
        fields = '__all__'

'''
def to_representation(self, instance):
    return{
        id:instance.id,
        image:instance.image if instance.image !='' or instance.image !=None else '',
    }

'''