from rest_framework import serializers

from app_products.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        # fields = [
        #     'id', 'name_product', 
        #     'desc_product', 
        #     'display_price', 'price', 'price_with_discount_or_PROMO',
        #     'display_discount', 'discount', 'discount_period', 
        #     'display_remaining_goods', 'remaining_goods', 
        #     'display_tag', 'tag',
        #     'display_promo', 'promo',
        #     'display_reviews', 'rating',
        # ]
        fields = "__all__"
        