from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.products.api.viewsets import ProductViewSet
from apps.products.api.views import ProductByIdAPIView

router  = DefaultRouter()

router.register(
    '', ProductViewSet, basename='products'
)
urlpatterns = [
    path('id/<int:pk>/', 
    ProductByIdAPIView.as_view(), 
    name='product-by-id')
]

urlpatterns += router.urls