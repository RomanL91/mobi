from collections import OrderedDict

from rest_framework import serializers

from app_basket.models import Basket

from app_products.serializers import ProductsSerializer


class BasketSerializer(serializers.ModelSerializer):
    products = ProductsSerializer()
    class Meta:
        model = Basket
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if isinstance(instance, OrderedDict):
            instance = Basket.objects.get(
                user_session=instance['user_session'],
                products=instance['products']
            )

        price_per_prod = instance.products.price_with_discount_or_PROMO
        total_price_per_position = instance.product_cost
        total_price_of_customer_cart = instance.total_cost
        representation['price_per_prod'] = price_per_prod
        representation['total_price_per_position'] = total_price_per_position
        representation['total_price_of_customer_cart'] = total_price_of_customer_cart

        return representation