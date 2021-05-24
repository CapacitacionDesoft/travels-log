from .views import LocationViewSet, MaterialViewSet, TravelViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('location', LocationViewSet, basename='location')
router.register('material', MaterialViewSet, basename='material')
router.register('travel', TravelViewSet, basename='travel')
urlpatterns = [
    path('', include(router.urls))
]