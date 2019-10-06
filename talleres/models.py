from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from django.utils.safestring import mark_safe
from location_field.models.plain import PlainLocationField

from company.models import Brand, Model
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

class ServiceType(models.Model):
    class Meta:
        verbose_name = 'Tipo de Servicio'
        verbose_name_plural = 'Tipos de Servicios'
    name = models.CharField(verbose_name='Nombre', max_length=100, null=True)

    def __str__(self):
        return str(self.name)


class Service(models.Model):
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    ID_TYPE = (('CHAPA','Chapa'), ('CHASIS','Chasis'))
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(verbose_name='Nombre', max_length=100, null=True)
    phone = models.CharField(verbose_name='Celular', max_length=100, null=True)
    email = models.CharField(verbose_name='Email', max_length=100, null=True)
    document = models.CharField(verbose_name='Documento', max_length=100, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Marca')
    model = models.ForeignKey(Model, on_delete=models.PROTECT, verbose_name='Modelo')
    year = models.PositiveSmallIntegerField(verbose_name='Año', null=True)
    car_km = models.PositiveIntegerField(null=True, verbose_name='Kilometraje')
    license_plate = models.CharField(verbose_name='Número', max_length=100, null=True)
    id_type = models.CharField(verbose_name='Tipo de Identificación', choices= ID_TYPE, max_length=100, null=True)
    workshop = models.ForeignKey(Taller, on_delete=models.PROTECT, null=True)
    comment = models.TextField(null=True, verbose_name='Comentario')
    date = models.DateField(null=True,verbose_name='Fecha')
    time = models.TimeField(null=True, verbose_name='Hora')

    def __str__(self):
        return str(self.name)

