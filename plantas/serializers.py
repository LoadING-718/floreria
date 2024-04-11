from rest_framework import serializers
from .models import PlantRegistry

class PlantRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantRegistry
        fields = '__all__'