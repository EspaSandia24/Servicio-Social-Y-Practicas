from django.db import models
from django.core.validators import FileExtensionValidator
from .validadores import documentos_validador
#from alumnos.models import Alumnos

TIPO=[
    ('','Elige el tipo'),
    ('SS','Servicio Social'),
    ('PP','Practicas Profecionales'),
]

class Datos(models.Model):
    alumno = models.ForeignKey('alumnos.Alumnos', verbose_name='Alumno', on_delete=models.DO_NOTHING)
    # institucion = models.CharField('Nombre', max_length=50)
    institucion = models.ForeignKey("instituciones.UnidadAcademica", verbose_name='Unidad Académica', on_delete=models.DO_NOTHING)
    tipo = models.CharField(max_length=2, choices=TIPO)
    fecha_inicio = models.DateField('Fecha de inicio', max_length=10,)
    fecha_termino = models.DateField('Fecha de termino', max_length=10,null=True, blank=True)
    kardex = models.FileField(upload_to='documentos/', validators=[documentos_validador])
    constancia_estudios = models.FileField(upload_to='documentos/', validators=[documentos_validador])
    carta_aceptacion = models.FileField(upload_to='documentos/', validators=[documentos_validador])
    carta_liberacion = models.FileField(upload_to='documentos/', validators=[documentos_validador],null=True, blank=True)
    #user = models.ForeignKey("usuarios.Aquí va el modelo", \
    #   verbose_name='Usuarios', on_delete=models.DO_NOTHING)

 
