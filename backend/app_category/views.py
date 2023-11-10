from app_category.models import Category

from app_category.serializers import CategorySerializer

from rest_framework import viewsets

from rest_framework.response import Response

from rest_framework.decorators import action

from app_products.serializers import ProductSerializerForCategory
 

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        obj = self.get_object()
        queryset = obj.products_set.all()
        self.serializer_class = ProductSerializerForCategory
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)