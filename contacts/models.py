from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from django.utils.safestring import mark_safe
from django.utils.timezone import now

from toyota.settings import MEDIA_URL


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    email = models.CharField(verbose_name='Email', max_length=100)
    message = models.TextField(verbose_name='Mensaje')
    created_at = models.DateTimeField('Fecha Creación',default=now)

    def __str__(self):
        return self.email

