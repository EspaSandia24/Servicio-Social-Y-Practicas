# Generated by Django 3.2.19 on 2023-05-09 01:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(max_length=10, verbose_name='Fecha de inicio')),
                ('fecha_termino', models.DateField(max_length=10, verbose_name='Fecha de termino')),
                ('kardex', models.FileField(upload_to='archivos/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('constancia_estudios', models.FileField(upload_to='archivos/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('carta_aceptacion', models.FileField(upload_to='archivos/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('carta_liberacion', models.FileField(upload_to='archivos/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
            ],
        ),
    ]