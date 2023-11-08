from rest_framework import viewsets

from app_basket.models import Basket

from app_basket.serializers import BasketSerializer

 

class BasketViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
