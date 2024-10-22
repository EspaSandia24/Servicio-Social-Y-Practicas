# Generated by Django 3.2.19 on 2023-05-09 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteMensual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('', '------'), ('SS', 'Servicio Social'), ('PP', 'Practicas Profecionales')], max_length=2)),
                ('actividades', models.CharField(max_length=300)),
                ('horas_Reportadas', models.IntegerField(default=0)),
                ('fecha_inicio', models.DateField(max_length=10, verbose_name='Fecha de inicio')),
                ('fecha_termino', models.DateField(max_length=10, verbose_name='Fecha de termino')),
                ('fecha', models.DateField(max_length=10, verbose_name='Fecha de entrega')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumnos.alumnos', verbose_name='Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='ReporteInicial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('', '------'), ('SS', 'Servicio Social'), ('PP', 'Practicas Profecionales')], max_length=2)),
                ('mes1', models.CharField(max_length=300)),
                ('mes2', models.CharField(max_length=300)),
                ('mes3', models.CharField(max_length=300)),
                ('mes4', models.CharField(max_length=300)),
                ('mes5', models.CharField(max_length=300)),
                ('mes6', models.CharField(max_length=300)),
                ('mes7', models.CharField(max_length=300)),
                ('mes8', models.CharField(max_length=300)),
                ('mes9', models.CharField(max_length=300)),
                ('mes10', models.CharField(max_length=300)),
                ('mes11', models.CharField(max_length=300)),
                ('mes12', models.CharField(max_length=300)),
                ('fecha', models.DateField(max_length=10, verbose_name='Fecha De Inicio')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumnos.alumnos', verbose_name='Alumno')),
            ],
        ),
    ]
