from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.products.selectors import get_products
from apps.products.api.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
)

class ProductViewSet(ReadOnlyModelViewSet):
    lookup_field = 'slug'
    serializer_classes = {
        'list': ProductListSerializer,
        'retrieve': ProductDetailSerializer,
    }
    def get_queryset(self):
        return get_products()
    
    def get_serializer_class(self):
        return self.serializer_classes.get(
            self.action,
            ProductListSerializer,
        )