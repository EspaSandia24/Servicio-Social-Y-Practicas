# Generated by Django 3.2.19 on 2023-05-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='ap_materno',
            field=models.CharField(max_length=20, verbose_name='Apellido materno'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='fecha_nac',
            field=models.DateField(max_length=10, verbose_name='Fecha de nacimiento'),
        ),
    ]
