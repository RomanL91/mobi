from rest_framework import serializers

from app_basket.models import Basket

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_price_per_position = instance.product_cost
        total_price_of_customer_cart = instance.total_cost
        representation['total_price_per_position'] = total_price_per_position
        representation['total_price_of_customer_cart'] = total_price_of_customer_cart

        return representation