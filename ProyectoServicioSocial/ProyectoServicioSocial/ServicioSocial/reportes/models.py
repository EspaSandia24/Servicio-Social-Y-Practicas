from django.db import models
from alumnos.models import Alumnos
from instituciones.models import Institucion

TIPO=[
    ('','------'),
    ('SS','Servicio Social'),
    ('PP','Practicas Profecionales'),
]

PUNTUACIONES_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
)



class ReporteInicial(models.Model): 
    alumno = models.ForeignKey("alumnos.Alumnos", verbose_name='Alumno', on_delete=models.DO_NOTHING)
    tipo = models.CharField(max_length=2, choices=TIPO)
    mes1 = models.CharField( max_length=300)
    mes2 = models.CharField( max_length=300)
    mes3 = models.CharField( max_length=300)
    mes4 = models.CharField( max_length=300)
    mes5 = models.CharField( max_length=300)
    mes6 = models.CharField( max_length=300)
    mes7 = models.CharField( max_length=300)
    mes8 = models.CharField( max_length=300)
    mes9 = models.CharField( max_length=300)
    mes10 = models.CharField( max_length=300)
    mes11 = models.CharField( max_length=300)
    mes12 = models.CharField( max_length=300)
    fecha = models.DateField('Fecha De Inicio', max_length=10)
    
class ReporteMensual(models.Model):
    alumno = models.ForeignKey("alumnos.Alumnos", verbose_name='Alumno', on_delete=models.DO_NOTHING)
    tipo = models.CharField(max_length=2, choices=TIPO)
    actividades = models.CharField( max_length=300)
    horas_Reportadas = models.IntegerField(default=00)
    fecha_inicio = models.DateField('Fecha de inicio', max_length=10)
    fecha_termino = models.DateField('Fecha de termino', max_length=10)
    fecha = models.DateField('Fecha de entrega', max_length=10)
    

ACTITUD_CHOICES = (
    (1, 'Totalmente indiferente'),
    (2, 'Indicaba que no sabía, pero no hacía nada'),
    (3, 'Indicaba que no sabía, pero buscaba una solución')
)

class EvaluacionFinal(models.Model):
    alumno = models.ForeignKey("alumnos.Alumnos", verbose_name='Alumno', on_delete=models.DO_NOTHING)
    fecha_inicio = models.DateField('Fecha de inicio')
    fecha_termino = models.DateField('Fecha de término')
    institucion = models.ForeignKey("instituciones.Institucion", verbose_name='Institución', on_delete=models.DO_NOTHING)
    puntualidad = models.IntegerField(choices=PUNTUACIONES_CHOICES, verbose_name='Puntuación para la puntualidad')
    cumplimiento_actividades = models.IntegerField(choices=PUNTUACIONES_CHOICES, verbose_name='Puntuación para el cumplimiento de actividades')
    actividades_ordenadas = models.IntegerField(choices=PUNTUACIONES_CHOICES, verbose_name='Puntuación para la realización ordenada de actividades')
    conocimientos_suficientes = models.IntegerField(choices=PUNTUACIONES_CHOICES, verbose_name='Puntuación para los conocimientos suficientes')
    comportamiento = models.IntegerField(choices=PUNTUACIONES_CHOICES, verbose_name='Puntuación para el comportamiento')
    actitud = models.IntegerField(choices=PUNTUACIONES_CHOICES, verbose_name='Puntuación para la actitud')
    actitud_actividad_desconocida = models.IntegerField(choices=ACTITUD_CHOICES, verbose_name='Actitud ante una actividad desconocida')
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Calificación')
    observaciones = models.CharField(max_length=200, verbose_name='Observaciones')