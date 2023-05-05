from django.db import models


class UnidadAcademica(models.Model):
    nombre = models.CharField('Nombre', max_length=200)
    direccion = models.CharField('Dirección', max_length=350, default='sin dirección')

    def __str__(self):
        return self.nombre 
    
    
class ProgramaAcademico(models.Model):
    clave = models.BigAutoField('Clave', primary_key=True)
    nombre = models.CharField('Nombre', max_length=200)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    telefono = models.CharField('Teléfono', max_length=10, blank=True, null=True)
    unidad_academica = models.ForeignKey("instituciones.UnidadAcademica", \
        verbose_name='Unidad Académica', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre 
    
class Institucion(models.Model):
    TIPO_CHOICES = (
        ('publico', 'Público'),
        ('privado', 'Privado')
    )
    clave = models.BigAutoField('Clave', primary_key=True)
    nombre = models.CharField('Nombre', max_length=200)
    direccion = models.CharField('Dirección', max_length=200)
    email = models.EmailField('Email', max_length=254)
    telefono = models.CharField('Teléfono', max_length=10)
    rfc = models.CharField('RFC', max_length=13)
    tipo = models.CharField('Tipo', max_length=7, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre
