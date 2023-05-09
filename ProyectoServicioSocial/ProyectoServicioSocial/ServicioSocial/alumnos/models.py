from django.db import models

class Alumnos(models.Model):
    matricula = models.CharField('Matrícula', max_length=8, primary_key=True)
    nombre = models.CharField('Nombre', max_length=50)
    ap_paterno = models.CharField('Apellido paterno', max_length=20)
    ap_materno = models.CharField('Apellido materno', max_length=20)
    fecha_nac = models.DateField('Fecha de nacimiento', max_length=10)
    #user = models.ForeignKey("usuarios.Aquí va el modelo", \
    #   verbose_name='Usuarios', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre
    
