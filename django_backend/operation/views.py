# Create your views here.
from rest_framework import generics, viewsets
from .serializers import TravelSerializers, MaterialSerializers, LocationSerializers
from .models import Travel, Material, Location
from rest_framework.permissions import AllowAny


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Location.objects.all()
    serializer_class = LocationSerializers


class MaterialViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Material.objects.all()
    serializer_class = MaterialSerializers


class TravelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Travel.objects.all()
    serializer_class = TravelSerializers

