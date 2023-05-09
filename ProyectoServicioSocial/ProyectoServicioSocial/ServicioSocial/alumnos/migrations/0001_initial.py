# Generated by Django 3.2.19 on 2023-05-09 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('matricula', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Matrícula')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('ap_paterno', models.CharField(max_length=20, verbose_name='Apellido paterno')),
                ('ap_materno', models.CharField(max_length=20, verbose_name='Apellido materno')),
                ('fecha_nac', models.DateField(max_length=10, verbose_name='Fecha de nacimiento')),
            ],
        ),
    ]
