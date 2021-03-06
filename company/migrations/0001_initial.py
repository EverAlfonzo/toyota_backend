# Generated by Django 2.2 on 2019-04-03 00:28

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('description', models.CharField(default='', max_length=200, verbose_name='Descripcion Breve')),
                ('large_description', models.TextField(verbose_name='Descripción Larga')),
                ('phone', models.CharField(default='', max_length=50, verbose_name='Teléfono')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('city', models.CharField(max_length=255, null=True, verbose_name='Ciudad')),
                ('location', location_field.models.plain.PlainLocationField(default='-25.3014877,-57.5804482', max_length=63, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/company/', verbose_name='Imagen')),
            ],
            options={
                'verbose_name_plural': 'Compañía',
                'verbose_name': 'Compañía',
            },
        ),
    ]
