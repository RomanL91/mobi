from app_products.models import Products

from app_products.serializers import ProductsSerializer

from rest_framework import viewsets
 
 
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
