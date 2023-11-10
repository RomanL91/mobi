from rest_framework import serializers

from app_color.models import Color

# from app_products.serializers import ProductSerializerForRiview


class ColorSerializer(serializers.ModelSerializer):
    # product = ProductSerializerForRiview()
    class Meta:
        model = Color
        fields = "__all__"
