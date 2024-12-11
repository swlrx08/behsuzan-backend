from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, SpecificationViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('specifications', SpecificationViewSet, basename='specification')

urlpatterns = [
    path('', include(router.urls)),
]
