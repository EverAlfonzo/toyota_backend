from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from toyota.settings import MEDIA_URL


class Profile(models.Model):
    class Meta:
        verbose_name_plural = 'Perfiles'
        verbose_name = 'Perfil'
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name='usuario')
    phone = models.CharField(max_length=100,verbose_name='Celular')
    image = models.ImageField('Imagen',blank=True, upload_to='images/profiles/', null=True)


    def __str__(self):
        return self.user.username

    def image_tag(self):
        return mark_safe('<img width="150" src="%s%s" />' % (MEDIA_URL, self.image or 'images/profiles/default.png'))

    image_tag.short_description = 'Vista Previa'
    image_tag.allow_tags = True
