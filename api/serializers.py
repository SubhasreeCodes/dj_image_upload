from rest_framework import serializers

from backend.models import Gallery


class GallerySerializer(serializers.ModelSerializers):
    class Meta:
        model = Gallery
        fields = ('image', )