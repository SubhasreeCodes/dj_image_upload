from django.contrib import admin
from django.utils.html import format_html

from backend.models import Gallery

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag')

    def image_tag(self, obj):
        return format_html('<img src ="{}" width="150" height="150" />'.format(obj.image.url))

    image_tag.short_description = "Image"

admin.site.register(Gallery, GalleryAdmin)