from django import forms
from datos.models import Datos
    
class FormDatos(forms.ModelForm):
    
    class Meta:
        model = Datos
        fields = '__all__'

class FormDatos(forms.ModelForm):
        
    class Meta:
        model = Datos
        fields = '__all__'
        exclude = []
        widgets = {
            'alumno': forms.Select(
                attrs={'class':'form-control','placeholder':'Alumno'}
            ),
            'unidad': forms.Select(
                attrs={'class':'form-control','placeholder':'Institución'}
            ),
            'institucion': forms.Select(
                attrs={'class':'form-control','placeholder':'Institución'}
            ),
            'tipo': forms.Select(
                attrs={'class':'form-control','placeholder':'Tipo'}
            ),
            'fecha_inicio': forms.TextInput(
                attrs={'class':'form-control','placeholder':'dd/mm/aaaa'}
            ),
            'fecha_termino': forms.TextInput(
                attrs={'class':'form-control','placeholder':'dd/mm/aaaa',"required": False}
            ),
            'kardex' : forms.FileInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Sólo archivos PDF'}
            ),
            'constancia_estudios' : forms.FileInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Sólo archivos PDF'}
            ),
            'carta_aceptacion' : forms.FileInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Sólo archivos PDF'}
            ),
            'carta_liberacion' : forms.FileInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Sólo archivos PDF',"required": False}
            ),
            #'user': forms.Select(
            #    attrs={'class':'form-control','placeholder':'User'}),
        }


class FormDatosEditar(FormDatos):
    class Meta:
        exclude = ['alumno']
        model = Datos

class FiltrosDatos(FormDatos):
    
    def __init__(self, *args, **kwargs):
        super(FiltrosDatos, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].required = False




