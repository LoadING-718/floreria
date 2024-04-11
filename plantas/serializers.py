from rest_framework import serializers
from .models import plantregistry

class PlantRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = plantregistry
        fields = '__all__'