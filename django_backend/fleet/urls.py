from .views import DriverViewSet, VehicleViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('driver', DriverViewSet, basename='driver')
router.register('vehicle', VehicleViewSet, basename='vehicle')
urlpatterns = [
    path('', include(router.urls))
]