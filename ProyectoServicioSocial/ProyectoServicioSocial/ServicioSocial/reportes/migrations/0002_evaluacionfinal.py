# Generated by Django 3.2.19 on 2023-05-26 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instituciones', '0001_initial'),
        ('alumnos', '0003_alter_alumnos_matricula'),
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio')),
                ('fecha_termino', models.DateField(verbose_name='Fecha de término')),
                ('puntualidad', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Puntuación para la puntualidad')),
                ('cumplimiento_actividades', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Puntuación para el cumplimiento de actividades')),
                ('actividades_ordenadas', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Puntuación para la realización ordenada de actividades')),
                ('conocimientos_suficientes', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Puntuación para los conocimientos suficientes')),
                ('comportamiento', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Puntuación para el comportamiento')),
                ('actitud', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Puntuación para la actitud')),
                ('actitud_actividad_desconocida', models.IntegerField(choices=[(1, 'Totalmente indiferente'), (2, 'Indicaba que no sabía, pero no hacía nada'), (3, 'Indicaba que no sabía, pero buscaba una solución')], verbose_name='Actitud ante una actividad desconocida')),
                ('calificacion', models.IntegerField(verbose_name='Calificación')),
                ('observaciones', models.CharField(max_length=200, verbose_name='Observaciones')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumnos.alumnos', verbose_name='Alumno')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instituciones.institucion', verbose_name='Institución')),
            ],
        ),
    ]
