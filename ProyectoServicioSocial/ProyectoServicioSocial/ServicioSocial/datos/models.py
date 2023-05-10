from django.db import models
from django.core.validators import FileExtensionValidator
from .validadores import documentos_validador

class Datos(models.Model):
    # alumno = models.CharField('Matrícula', max_length=8, primary_key=True)
    # institucion = models.CharField('Nombre', max_length=50)
    fecha_inicio = models.DateField('Fecha de inicio', max_length=10,null=False, blank=False)
    fecha_termino = models.DateField('Fecha de termino', max_length=10, null=True, blank=True)
    kardex = models.FileField(upload_to='documentos/', null=False,blank=False, validators=[documentos_validador])
    constancia_estudios = models.FileField(upload_to='documentos/', null=False,blank=False, validators=[documentos_validador])
    carta_aceptacion = models.FileField(upload_to='documentos/', null=False,blank=False, validators=[documentos_validador])
    carta_liberacion = models.FileField(upload_to='documentos/', null=False,blank=False, validators=[documentos_validador])
    
    #user = models.ForeignKey("usuarios.Aquí va el modelo", \
    #   verbose_name='Usuarios', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre
    
