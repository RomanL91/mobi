from rest_framework import viewsets

from app_color.models import Color

from app_color.serializers import ColorSerializer


class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
