# Generated by Django 3.2.19 on 2023-06-06 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instituciones', '0001_initial'),
        ('alumnos', '0004_auto_20230606_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='programa_academico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instituciones.programaacademico', verbose_name='Programa Academico'),
        ),
    ]
