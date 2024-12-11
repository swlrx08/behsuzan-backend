from rest_framework import viewsets
from .models import Product, Specification
from .serializers import ProductSerializer, SpecificationSerializer, ProductGetSerializer
from django_filters.rest_framework import DjangoFilterBackend


class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('specifications').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProductGetSerializer
        elif self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return ProductSerializer

        return super().get_serializer_class()
