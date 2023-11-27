from collections import OrderedDict

from rest_framework import serializers

from app_basket.models import Basket


class BasketSerializer(serializers.ModelSerializer):
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

        name_product = instance.products.name_product
        product_images = [
            i.image.url for i in instance.products.productimage_set.all()]
        
        price_per_prod = instance.products.price
        display_discount = instance.products.display_discount
        if instance.products.display_discount:
            price_per_prod -= price_per_prod * (instance.products.discount / 100)

        representation['name_product'] = name_product
        representation['product_images'] = product_images
        representation['price_per_prod'] = price_per_prod
        representation['display_discount'] = display_discount
        representation['display_promo'] = instance.products.display_promo
        if instance.products.display_promo:
            representation['price_per_promo'] = instance.products.price_with_discount_or_PROMO

        return representation
    