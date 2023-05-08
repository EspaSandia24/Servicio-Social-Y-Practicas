from django.db import models
from alumnos.models import Alumnos

TIPO=[
    ('','------'),
    ('SS','Servicio Social'),
    ('PP','Practicas Profecionales'),
]

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
    horas_Reportadas = models.IntegerField(default=0,max_length=80)
    fecha_inicio = models.DateField('Fecha de inicio', max_length=10)
    fecha_termino = models.DateField('Fecha de termino', max_length=10)
    fecha = models.DateField('Fecha de entrega', max_length=10)
    