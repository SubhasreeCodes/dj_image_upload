from django.urls import path

from api.views import GalleryViewSet

urlpatterns = [

    # Image
    path('image/gallery/', GalleryViewSet.as_view(), name='image_gallery'),
    path('image/upload/', GalleryViewSet.as_view(), name='image_upload')

]