# Generated by Django 2.2.6 on 2019-10-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_delivery_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='comment',
            field=models.TextField(null=True, verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='date',
            field=models.DateField(null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='number',
            field=models.PositiveIntegerField(null=True, verbose_name='Número de Casa'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='time',
            field=models.TimeField(null=True, verbose_name='Hora'),
        ),
    ]
