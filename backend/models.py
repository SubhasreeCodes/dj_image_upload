from django.db import models

# Create your models here.

class Gallery(models.Model):
    id = models.BigAutoField(primary_key=True)

    image = models.ImageField(upload_to="gallery/", blank=True, null=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/language/%s" width="150" height="150" />'%(self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = 'gallery'
