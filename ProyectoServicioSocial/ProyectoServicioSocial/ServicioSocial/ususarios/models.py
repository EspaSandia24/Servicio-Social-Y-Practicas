from django.db import models
from ususarios.validadores import rfc_validator, curp_validator
from django.contrib.auth.models import User


class DatosPersonales(models.Model):
    rfc = models.CharField("R.F.C.", max_length=13, validators=[rfc_validator])
    curp = models.CharField("C.U.R.P.", max_length=18, validators=[curp_validator])
    telefono = models.CharField("Teléfono", max_length=10)
    foto = models.ImageField(upload_to='perfil')
    usuario = models.OneToOneField(User, verbose_name="Usuario", related_name='datos', on_delete=models.DO_NOTHING)