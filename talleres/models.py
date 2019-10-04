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

    title = models.CharField(verbose_name='Título', max_length=100, unique=True)
    address = models.CharField(max_length=200, verbose_name='Dirección')
    image = models.ImageField('Imagen', upload_to='images/talleres/', null=True)
    phones = models.CharField(verbose_name='Teléfonos',null=True, max_length=100,
                              help_text='los teléfonos pueden ir separados por comas')

    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Ciudad')
    location = PlainLocationField(based_fields=['city'], zoom=7, null=True, default='-25.3014877,-57.5804482')
    # location = GeopositionField()

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img width="150" src="%s%s" />' % (MEDIA_URL, self.image or 'images/talleres/default.png'))

    image_tag.short_description = 'Vista Previa'
    image_tag.allow_tags = True
