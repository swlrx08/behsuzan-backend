from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, SpecificationViewSet, ProductImagesViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('specifications', SpecificationViewSet, basename='specification')
router.register('products-images', ProductImagesViewSet, basename='products-images')

urlpatterns = [
    path('', include(router.urls)),
]
