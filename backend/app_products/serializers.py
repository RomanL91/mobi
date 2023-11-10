from rest_framework import serializers

from app_products.models import Products, ProductImage

from app_category.serializers import CategorySerializer
from app_tags.serializers import TagSerializer
from app_promo.serializers import PromoSerializer
from app_color.serializers import ColorSerializer


class ProductSerializerForCategory(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ProductSerializerForRiview(serializers.ModelSerializer):
    category = CategorySerializer()
    tag = TagSerializer(many=True)
    class Meta:
        model = Products
        fields = [
            'category',
            'name_product',
            'tag',
        ]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tag = TagSerializer(many=True)
    promo = PromoSerializer()
    color =ColorSerializer()
    class Meta:
        model = Products
        fields = "__all__"


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        all_entity_image_product = instance.productimage_set.all()
        list_url_to_image = [
            image.image.url for image in all_entity_image_product
        ]
        representation['list_url_to_image'] = list_url_to_image

        if not instance.display_price:
            del representation['display_price']
            del representation['price']

        if not instance.display_discount:
            del representation['display_discount']
            del representation['discount']
            del representation['discount_period']

        if not instance.display_remaining_goods:
            del representation['display_remaining_goods']
            del representation['remaining_goods']

        if not instance.display_tag:
            del representation['display_tag']
            del representation['tag']

        if not instance.display_promo:
            del representation['display_promo']
            del representation['promo']

        if not instance.display_reviews:
            del representation['display_reviews']
            del representation['rating']
            
        return representation
