from django.contrib.auth.models import User
from django.db import models
# from location_field.models.spatial import LocationField
# from django.contrib.gis.geos import Point
from django.utils.safestring import mark_safe
from location_field.models.plain import PlainLocationField
from toyota.settings import MEDIA_URL

# Create your models here.
class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Compañía'
        verbose_name = 'Compañía'
    name = models.CharField(verbose_name='Nombre',max_length=100,unique=True)
    description = models.CharField(verbose_name='Descripcion Breve',max_length=200,default='')
    large_description = models.TextField(verbose_name='Descripción Larga')
    phone = models.CharField(verbose_name='Teléfono',max_length=50,default='')
    address = models.CharField(verbose_name='Dirección',max_length=200)
    city = models.CharField(verbose_name='Ciudad',max_length=255,null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7,null=True,default='-25.3014877,-57.5804482')
    image = models.ImageField('Imagen',upload_to='images/company/',null=True)

    def image_tag(self):
        return mark_safe('<img width="150" src="%s%s" />' % (MEDIA_URL, self.image or 'images/default.png'))


    image_tag.short_description = 'Vista Previa'
    image_tag.allow_tags = True



    def __str__(self):
        return self.name

class CompanyImage(models.Model):
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    image = models.ImageField('Imagen', upload_to='images/company/', null=True)

    def image_tag(self):
        return mark_safe('<img width="150" src="%s%s" />' % (MEDIA_URL, self.image or 'images/default.png'))


    image_tag.short_description = 'Vista Previa'
    image_tag.allow_tags = True



# Create your models here.
class Brand(models.Model):
    class Meta:
        verbose_name_plural = 'Marcas'
        verbose_name = 'Marca'
    name = models.CharField(verbose_name='Nombre',max_length=100,unique=True)
    image = models.ImageField('Imagen',upload_to='images/brands/',null=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img width="150" src="%s%s" />' % (MEDIA_URL, self.image or 'images/default.png'))

    image_tag.short_description = 'Vista Previa'
    image_tag.allow_tags = True


class Model(models.Model):
    class Meta:
        verbose_name_plural = 'Modelos'
        verbose_name = 'Modelo'

    name = models.CharField(verbose_name='Nombre', max_length=100, unique=True)
    brand = models.ForeignKey(Brand, verbose_name='Marca', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name



class Delivery(models.Model):
    class Meta:
        verbose_name_plural = 'Mantenimientos Express'
        verbose_name = 'Mantenimiento Express'
    user = models.ForeignKey(User, verbose_name='usuario', on_delete=models.PROTECT)
    number = models.PositiveIntegerField(null=True, verbose_name='Número de Casa')
    date = models.DateField(null=True, verbose_name='Fecha')
    time = models.TimeField(null=True,verbose_name='Hora')
    comment = models.TextField(null=True,verbose_name='Comentario')
    location = PlainLocationField(zoom=7, null=True, default='-25.3014877,-57.5804482')

    def __str__(self):
        return "%s - %s"%(self.date.strftime('%d/%m/%Y'),self.user.__str__())