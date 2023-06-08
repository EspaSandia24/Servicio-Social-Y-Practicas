from django import forms
from asesores.models import Asesores


class FormAsesores(forms.ModelForm):
    
    class Meta:
        model = Asesores
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Nombre(s)'}
            ),
            'ap_paterno': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Apellido paterno'}
            ),
            'ap_materno': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Apellido materno'}
            ),
            'institucion': forms.Select(
                attrs={'class':'form-control','placeholder':'Institución'}
            ),
            'puesto': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Puesto'}
            ),
            #'user': forms.Select(
            #    attrs={'class':'form-control','placeholder':'User'}),
            'telefono': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Teléfono'}
            ),
            'no_serie': forms.TextInput(
                attrs={'class':'form-control','placeholder':'No. Serie'}
            ),
            'certificado': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Certificado'}
            ),
            'contrasena_cert': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Contraseña de Certificado'}
            ),
            'tipo': forms.Select(
                attrs={'class':'form-control','placeholder':'Tipo'}
            ),
        }

class FormAsesoresEditar(FormAsesores):
    class Meta:
        exclude = ['id']
        model = Asesores

class FiltrosAsesores(FormAsesores):
    
    def __init__(self, *args, **kwargs):
        super(FiltrosAsesores, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].required = False