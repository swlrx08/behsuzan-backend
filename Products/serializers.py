from rest_framework import serializers
from .models import Product, Specification, ProductImages


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ['id', 'key', 'value']


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'images', 'product']


class ProductSerializer(serializers.ModelSerializer):
    specifications = SpecificationSerializer(many=True, required=True)  # مشخصات به صورت لیست JSON
    p_images = ProductImagesSerializer(many=True, required=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'short_description', 'specifications', 'p_images']

    def create(self, validated_data):
        # Extract specifications data
        specifications_data = validated_data.pop('specifications')
        images_data = validated_data.pop('p_images', [])

        # Create the Product instance
        product = Product.objects.create(**validated_data)

        # Create related Specification instances
        for spec_data in specifications_data:
            product.specifications.create(**spec_data)

        if images_data:
            image_instances = [ProductImages(product=product, **image_data) for image_data in images_data]
            ProductImages.objects.bulk_create(image_instances)

        return product

    def update(self, instance, validated_data):
        # Extract specifications data
        specifications_data = validated_data.pop('specifications', None)

        # Update the Product instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update, create, or delete specifications
        if specifications_data is not None:
            existing_spec_ids = [spec.id for spec in instance.specifications.all()]
            received_spec_ids = []

            for spec_data in specifications_data:
                spec_id = spec_data.get('id')  # Assuming 'id' is a field in Specification model
                if spec_id:
                    received_spec_ids.append(spec_id)
                    # Update existing specification
                    spec_instance = instance.specifications.get(id=spec_id)
                    for attr, value in spec_data.items():
                        setattr(spec_instance, attr, value)
                    spec_instance.save()
                else:
                    # Create new specification
                    new_spec = instance.specifications.create(**spec_data)
                    received_spec_ids.append(new_spec.id)

            # Delete specifications that were not included in the request
            for spec_id in existing_spec_ids:
                if spec_id not in received_spec_ids:
                    instance.specifications.get(id=spec_id).delete()

        return instance


class ProductGetSerializer(serializers.ModelSerializer):
    specifications = SpecificationSerializer(many=True)  # مشخصات به صورت لیست JSON

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'short_description', 'specifications']
