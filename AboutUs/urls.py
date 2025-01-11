from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AboutUsViewSet

router = DefaultRouter()
router.register('', AboutUsViewSet, basename='about_us')

urlpatterns = [
    path('', include(router.urls)),
]
