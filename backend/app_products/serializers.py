from rest_framework import serializers

from app_products.models import Products, ProductImage

from app_category.serializers import CategorySerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Products
    #     fields = [
    #         'id', 'name_product', 
    #         'desc_product', 
    #         'display_price', 'price', 'price_with_discount_or_PROMO',
    #         'display_discount', 'discount', 'discount_period', 
    #         'display_remaining_goods', 'remaining_goods', 
    #         'display_tag', 'tag',
    #         'display_promo', 'promo',
    #         'display_reviews', 'rating',
    #     ]
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        all_entity_image_product = instance.productimage_set.all()
        list_url_to_image = [
            image.image.url for image in all_entity_image_product
        ]
        representation['list_url_to_image'] = list_url_to_image
        return representation
