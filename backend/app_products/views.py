from rest_framework import viewsets

from app_products.models import Products, ProductImage

from app_products.serializers import ProductsSerializer, ProductImageSerializer
from app_reviews.serializers import ReviewSerializer

from rest_framework.response import Response

from rest_framework.decorators import action
 
 
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None, *args):
        queryset = self.get_object().review_set.all()
        self.serializer_class = ReviewSerializer
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
