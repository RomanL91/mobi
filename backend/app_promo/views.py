from rest_framework import viewsets

from app_promo.models import Promo

from app_promo.serializers import PromoSerializer


class PromoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
    