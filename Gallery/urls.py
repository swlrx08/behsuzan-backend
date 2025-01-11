from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryImageViewSet

router = DefaultRouter()
router.register('', GalleryImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
