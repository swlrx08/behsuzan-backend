from rest_framework import serializers
from .models import Product, Specification


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ['id', 'key', 'value']


class ProductSerializer(serializers.ModelSerializer):
    specifications = SpecificationSerializer(many=True)  # مشخصات به صورت لیست JSON

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'specifications', 'created_at']


class ProductGetSerializer(serializers.ModelSerializer):
    specifications = SpecificationSerializer(many=True)  # مشخصات به صورت لیست JSON

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'specifications', 'created_at']
