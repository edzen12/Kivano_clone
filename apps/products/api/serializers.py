from rest_framework import serializers
from apps.catalog.models import Category
from apps.products.models import (
    Product, Brand, ProductImage, ProductAttribute
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


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


class ProductAttributeSerializer(serializers.ModelSerializer):
    attribute = serializers.ModelSerializer(read_only=True)
    class Meta:
        model = ProductAttribute
        fields = ('attribute', 'value')


class ProductDetailSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(
        many=True, read_only=True
    )
    attributes = ProductAttributeSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'description',
            'category', 'brand',
            'images', 'attributes',
            'price', 'old_price',
            'stock_status', 'views_count', 'warranty'
        )