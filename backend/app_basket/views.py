from rest_framework import viewsets

from app_basket.models import Basket

from app_basket.serializers import BasketSerializer

 

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user_session=self.request.session.__dict__["_SessionBase__session_key"])
        return query_set
