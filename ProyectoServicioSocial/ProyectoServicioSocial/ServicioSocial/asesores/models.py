from django.db import models

TIPO=[
    ('','Elige el tipo'),
    ('INT','Interno'),
    ('EXT','Externo'),
]

class Asesores(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    ap_paterno = models.CharField('Apellido paterno', max_length=20)
    ap_materno = models.CharField('Apellido materno', max_length=20)
    institucion = models.ForeignKey("instituciones.Institucion", verbose_name='Institución', on_delete=models.DO_NOTHING)
    puesto = models.CharField('Puesto', max_length=30)
    #user = models.ForeignKey("usuarios.Aquí va el modelo", \
    #   verbose_name='Usuarios', on_delete=models.DO_NOTHING)
    telefono = models.CharField('Teléfono', max_length=10)
    no_serie = models.CharField('No. Serie', max_length=20)
    certificado = models.CharField('Certificado', max_length=3000)
    contrasena_cert = models.CharField('Contraseña de Certificado', max_length=20)
    tipo = models.CharField(max_length=3, choices=TIPO)
