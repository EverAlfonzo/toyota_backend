from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from django.utils.safestring import mark_safe
from location_field.models.plain import PlainLocationField

from location.models import City
from toyota.settings import MEDIA_URL


class Taller(models.Model):
    class Meta:
        verbose_name = 'Taller'
        verbose_name_plural = 'Talleres'

    address = models.CharField(max_length=200, verbose_name='Dirección',null=True)
    image = models.ImageField('Imagen', upload_to='images/talleres/', null=True)
    name = models.CharField(verbose_name='Nombre', max_length=100, unique=True,null=True)
    description = models.CharField(verbose_name='Descripcion Breve', max_length=200, default='', null=True, blank=True)
    large_description = models.TextField(verbose_name='Descripción Larga', null=True, blank=True)
    phone = models.CharField(verbose_name='Teléfono', max_length=50, default='')
    phone2 = models.CharField(verbose_name='Teléfono', max_length=50, default='', null=True, blank=True)

    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Ciudad')
    location = PlainLocationField(based_fields=['city'], zoom=7, null=True, default='-25.3014877,-57.5804482')

    def __str__(self):
        return str(self.name)

    def image_tag(self):
        return mark_safe('<img width="150" src="%s%s" />' % (MEDIA_URL, self.image or 'images/talleres/default.png'))

    image_tag.short_description = 'Vista Previa'
    image_tag.allow_tags = True
