# Generated by Django 3.2.19 on 2023-05-09 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0004_alter_datos_fecha_termino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='fecha_termino',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de termino'),
        ),
    ]