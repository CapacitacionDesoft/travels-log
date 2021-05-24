from rest_framework import serializers
from .models import Material, Location, Travel


class MaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class TravelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'