# Create your views here.
from rest_framework import generics, viewsets
from .serializers import DriverSerializers, VehicleSerializers
from .models import Driver, Vehicle
from rest_framework.permissions import AllowAny


class DriverViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Driver.objects.all()
    serializer_class = DriverSerializers


class VehicleViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializers
