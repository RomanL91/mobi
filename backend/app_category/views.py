from app_category.models import Category
from app_category.serializers import CategorySerializer

from app_products.serializers import ProductsSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        obj = self.get_object()
        queryset = obj.products_set.all()
        self.serializer_class = ProductsSerializer
        serializer = self.get_serializer(queryset, many=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)
    