from rest_framework import serializers

from app_reviews.models import Review

from app_products.serializers import ProductSerializerForRiview


class ReviewSerializer(serializers.ModelSerializer):
    # product = ProductSerializerForRiview()
    class Meta:
        model = Review
        fields = [
           'id', 'rating', 'review', 'phone_number', 'product'
        ]
