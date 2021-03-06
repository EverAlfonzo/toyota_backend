# Generated by Django 2.2.6 on 2019-10-06 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20191005_2013'),
        ('talleres', '0008_service_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='model',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='company.Model', verbose_name='Modelo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Brand', verbose_name='Marca'),
        ),
    ]
