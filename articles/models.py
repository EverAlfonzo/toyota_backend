from django.db import models
# Create your models here.
from django.utils.safestring import mark_safe
from django.utils.timezone import now

from toyota.settings import MEDIA_URL


class Article(models.Model):
    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    title = models.CharField(verbose_name='Título', max_length=100, unique=True)
    content = models.TextField(verbose_name='Contenido')
    created_at = models.DateTimeField('Fecha Creación',default=now)
    image = models.ImageField('Imagen', upload_to='images/articles/', null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img width="150" src="%s%s" />' % (MEDIA_URL, self.image or 'images/default.png'))

    image_tag.short_description = 'Vista Previa'
    image_tag.allow_tags = True
