# Generated by Django 4.0.4 on 2022-05-24 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivo',
            name='germinacion_1',
            field=models.IntegerField(verbose_name='Tiempo en dias de primera cosecha.'),
        ),
        migrations.AlterField(
            model_name='cultivo',
            name='germinacion_n',
            field=models.IntegerField(verbose_name='Tiempo en dias entre cosechas.'),
        ),
    ]
