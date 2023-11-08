from rest_framework import viewsets

from app_reviews.models import Review

from app_reviews.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
