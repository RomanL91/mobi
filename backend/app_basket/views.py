from app_basket.models import Basket
from app_products.models import Products

from app_basket.serializers import BasketSerializer

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    
    def create(self, request, *args, **kwargs):
        prod = Basket.objects.get_or_create(
                user_session=request.data['user_session'], 
                products=Products.objects.get(pk=request.data['products']))
        prod, flag = prod

        if flag:
            prod.quantity = int(request.data['quantity'])
            prod.save()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            prod.quantity = int(request.data['quantity'])
            prod.save()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


    @action(detail=False, methods=['get'])
    def visitor(self, request, pk=None):
        queryset = self.get_queryset().filter(user_session=request.session.__dict__["_SessionBase__session_key"])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
