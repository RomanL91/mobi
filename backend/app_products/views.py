from app_products.models import Products, ProductImage

from app_products.serializers import ProductsSerializer, ProductImageSerializer

from rest_framework import viewsets
 
 
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
