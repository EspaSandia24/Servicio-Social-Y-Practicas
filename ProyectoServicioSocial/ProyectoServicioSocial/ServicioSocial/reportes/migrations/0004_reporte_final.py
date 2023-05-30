# Generated by Django 3.2.19 on 2023-05-30 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_alter_alumnos_matricula'),
        ('reportes', '0003_alter_evaluacionfinal_calificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte_Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(max_length=10, verbose_name='Fecha de inicio')),
                ('fecha_termino', models.DateField(max_length=10, verbose_name='Fecha de termino')),
                ('horas_Acumuladas', models.IntegerField(default=0)),
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
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumnos.alumnos', verbose_name='Alumno')),
            ],
        ),
    ]
