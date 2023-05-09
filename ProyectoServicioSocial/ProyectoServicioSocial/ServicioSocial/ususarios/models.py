from django.db import models
from ususarios.validadores import rfc_validator, curp_validator
from django.contrib.auth.models import User


class DatosPersonales(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    ap_paterno = models.CharField('Apellido paterno',max_length=100)
    ap_materno = models.CharField('Apellido materno',max_length=100)
    fecha_nac = models.DateField('Fecha de Nacimiento', max_length=10)
    foto = models.ImageField("Foto de perfil", upload_to='perfil')
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.DO_NOTHING)