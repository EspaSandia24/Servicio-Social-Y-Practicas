from django import forms
from instituciones.models import ProgramaAcademico, UnidadAcademica

class FormProgramaAcademico(forms.ModelForm):
    
    class Meta:
        model = ProgramaAcademico
        fields = '__all__'
        # fields = ['clave, nombre']

class FormUnidadAcademica(forms.ModelForm):
    
    class Meta:
        model = UnidadAcademica
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Nombre'}
            ),
            'direccion': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Dirección'}
            ),
        }


class FormUnidadAcademicaEditar(FormUnidadAcademica):
    class Meta:
        model = UnidadAcademica
        fields = '__all__'

class FiltrosUnidadAcademica(FormUnidadAcademica):
    
    def __init__(self, *args, **kwargs):
        super(FiltrosUnidadAcademica, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].required = False