from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
import json
from api.serializers import GallerySerializer
from backend.models import Gallery


# Create your views here.

class GalleryViewSet(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def list(self, request, *args, **kwargs):
        gallery_images = Gallery.objects.all()
        serializer = GallerySerializer(gallery_images, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Gallery.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)