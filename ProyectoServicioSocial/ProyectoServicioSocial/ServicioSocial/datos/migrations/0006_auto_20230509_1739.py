# Generated by Django 3.2.19 on 2023-05-09 17:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0005_alter_datos_fecha_termino'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos',
            name='carta_aceptacion',
            field=models.FileField(blank=True, null=True, upload_to='documentos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'], message='Sólo se permiten documentos PDF')]),
        ),
        migrations.AddField(
            model_name='datos',
            name='carta_liberacion',
            field=models.FileField(blank=True, null=True, upload_to='documentos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'], message='Sólo se permiten documentos PDF')]),
        ),
        migrations.AddField(
            model_name='datos',
            name='constancia_estudios',
            field=models.FileField(default=2, upload_to='documentos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'], message='Sólo se permiten documentos PDF')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='datos',
            name='fecha_termino',
            field=models.DateField(blank=True, max_length=10, null=True, verbose_name='Fecha de termino'),
        ),
        migrations.AlterField(
            model_name='datos',
            name='kardex',
            field=models.FileField(upload_to='documentos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'], message='Sólo se permiten documentos PDF')]),
        ),
    ]
