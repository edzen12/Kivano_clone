from rest_framework import serializers
from apps.products.models import (
    Product, Brand, ProductImage
)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id','name', 'slug'
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id','image', 'is_main'
        )


class ProductListSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'price',
            'old_price', 'brand'
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    images = ProductImageSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'