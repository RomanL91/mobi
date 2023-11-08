from app_category.models import Category

from app_category.serializers import CategorySerializer

from rest_framework import viewsets
 

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
