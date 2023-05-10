# Generated by Django 3.2.19 on 2023-05-09 05:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datos',
            name='carta_aceptacion',
        ),
        migrations.RemoveField(
            model_name='datos',
            name='carta_liberacion',
        ),
        migrations.RemoveField(
            model_name='datos',
            name='constancia_estudios',
        ),
        migrations.AlterField(
            model_name='datos',
            name='fecha_termino',
            field=models.DateField(blank=True, max_length=10, null=True, verbose_name='Fecha de termino'),
        ),
        migrations.AlterField(
            model_name='datos',
            name='kardex',
            field=models.FileField(upload_to='Documentos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'], message='Sólo se permiten documentos PDF')]),
        ),
    ]