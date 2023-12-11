from app_basket.models import Basket, Order
from app_products.models import Products

from app_basket.serializers import BasketSerializer, OrderSerializer

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
        id_req = None
        promo = None
        for param in request.GET:
            if param == 'id':
                id_req = request.GET['id']
            if param == 'promo':
                promo = request.GET['promo']
                                    #http://localhost:8000/api/v1/basket/visitor/?buy=77714648717 и хешировать с солью(как идея просто)
                                    # http://localhost:8000/api/v1/basket/visitor/?buy=77714648717&promo=PROMO
        queryset = self.get_queryset().filter(user_session=id_req)
        for i in queryset:
            if i.products.promo is not None:
                if i.products.promo.pass_promo == promo:
                    i.promo_active = True
                else:
                    i.promo_active = False
                i.save()
                    
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        items = Basket.objects.filter(user_session=request.POST['user_session'])
        order_product_list = [
            {
               'products': el.products.name_product,  
               'quantity': el.quantity, 
               'add_datetime': el.add_datetime.strftime("%m/%d/%Y, %H:%M:%S"), 
               'promo_active': el.promo_active, 
            } for el in items
        ]
        totalcost = sum([
            item.product_cost for item in items
        ])

        prod, flag = Order.objects.get_or_create(
            user_session = request.POST['user_session'],
            user_name = request.POST['user_name'],
            user_telephone = request.POST['user_telephone'],
            order_delivery = bool(request.POST['order_delivery_address']),
            order_delivery_address = request.POST['order_delivery_address'],
            order_total_price = totalcost,
            promo = request.POST['promo'],
            order_product_list = order_product_list,
            completed = False
        )
        if flag:
            return Response({}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_200_OK)
