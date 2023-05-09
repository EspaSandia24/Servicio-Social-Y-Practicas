from django import forms
from alumnos.models import Alumnos

class FormAlumnos(forms.ModelForm):
    
    class Meta:
        model = Alumnos
        fields = '__all__'
        # fields = ['matricula, nombre']



class FormAlumnos(forms.ModelForm):
    
    class Meta:
        model = Alumnos
        fields = '__all__'
        
        widgets = {
            'matricula': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Matrícula'}
            ),
            'nombre': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Nombre(s)'}
            ),
            'ap_paterno': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Apellido paterno'}
            ),
            'ap_materno': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Apellido materno'}
            ),
            'fecha_nac': forms.TextInput(
                attrs={'class':'form-control','placeholder':'dd/mm/aaaa'}
            ),
            #'user': forms.Select(
            #    attrs={'class':'form-control','placeholder':'User'}),
        }

class FormAlumnosEditar(FormAlumnos):
    class Meta:
        exclude = ['matricula']
        model = Alumnos

class FiltrosAlumnos(FormAlumnos):
    
    def __init__(self, *args, **kwargs):
        super(FiltrosAlumnos, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].required = False