# Generated by Django 3.2.19 on 2023-06-08 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instituciones', '0001_initial'),
        ('asesores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asesores',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instituciones.institucion', verbose_name='Institución'),
        ),
    ]
