from rest_framework import viewsets

from app_tags.models import Tags

from app_tags.serializers import TagSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
