from django.db import models

class Department(models.Model):
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    name = models.CharField(verbose_name='Nombre', max_length=100, unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    department = models.ForeignKey(Department,verbose_name="Departamento",null=True,on_delete=models.SET_NULL)
    name = models.CharField(verbose_name='Nombre', max_length=100, unique=True)

    def __str__(self):
        return self.name
