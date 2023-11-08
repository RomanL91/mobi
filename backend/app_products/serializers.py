from rest_framework import serializers

from app_products.models import Products, ProductImage

from app_category.serializers import CategorySerializer
from app_tags.serializers import TagSerializer
from app_promo.serializers import PromoSerializer


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
    class Meta:
        model = Products
        fields = "__all__"


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        all_entity_image_product = instance.productimage_set.all()
        all_entity_colors_product = instance.color_set.all()
        list_url_to_image = [
            image.image.url for image in all_entity_image_product
        ]
        list_color_to_product = [
            {'color_name': el.name_color, 'color_code': el.color} for el in all_entity_colors_product
        ]
        representation['list_url_to_image'] = list_url_to_image
        representation['all_colors_product'] = list_color_to_product
        return representation
