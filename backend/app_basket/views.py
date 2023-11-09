from rest_framework import viewsets

from app_basket.models import Basket

from app_basket.serializers import BasketSerializer

from rest_framework.response import Response

from rest_framework.decorators import action

from rest_framework import status


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    
    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user_session=request.session.__dict__["_SessionBase__session_key"])
        set_buy = set([el.products.pk for el in queryset])

        if int(request.data['products']) in set_buy:
            prod = queryset.get(products=int(request.data['products']))

            self.lookup_field = 'pk'
            self.kwargs['pk'] = prod.pk
            
            self.update(request)

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    @action(detail=False, methods=['get'])
    def visitor(self, request, pk=None):
        queryset = self.get_queryset().filter(user_session=request.session.__dict__["_SessionBase__session_key"])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
