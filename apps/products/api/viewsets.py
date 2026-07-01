from apps.common.api.viewsets import BasedReadOnlyModelViewSet
from apps.products.selectors import get_products
from apps.products.api.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
)

class ProductViewSet(BasedReadOnlyModelViewSet):
    lookup_field = 'slug'
    serializer_classes = {
        'list': ProductListSerializer,
        'retrieve': ProductDetailSerializer,
    }
    def get_queryset(self):
        return get_products()
