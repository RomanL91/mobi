from rest_framework import viewsets

from app_basket.models import Basket

from app_basket.serializers import BasketSerializer

from rest_framework.response import Response

from rest_framework.decorators import action


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


    @action(detail=False, methods=['get'])
    def visitor(self, request, pk=None):
        queryset = Basket.objects.filter(user_session=request.session.__dict__["_SessionBase__session_key"])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
