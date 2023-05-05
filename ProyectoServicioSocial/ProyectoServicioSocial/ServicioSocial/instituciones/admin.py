from django.contrib import admin

# Register your models here.
from instituciones.models import UnidadAcademica, ProgramaAcademico, Institucion

admin.site.register(UnidadAcademica)
admin.site.register(ProgramaAcademico)
admin.site.register(Institucion)