from django.db import models
from instituciones.models import ProgramaAcademico

class Alumnos(models.Model):
    matricula = models.CharField('Matrícula', max_length=8, primary_key=True)
    nombre = models.CharField('Nombre', max_length=50)
    ap_paterno = models.CharField('Apellido paterno', max_length=20)
    ap_materno = models.CharField('Apellido materno', max_length=20)
    fecha_nac = models.DateField('Fecha de nacimiento', max_length=10)
    programa_academico = models.ForeignKey("instituciones.ProgramaAcademico",verbose_name='Programa Academico', null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.matricula
