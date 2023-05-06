from django import forms
from instituciones.models import ProgramaAcademico, UnidadAcademica, Institucion


class FormInstitucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'
        # fields = ['clave, nombre']

class FormInstitucion(forms.ModelForm):
    
    class Meta:
        model = Institucion
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Nombre'}
            ),
            'direccion': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Dirección'}
            ),
            'email': forms.EmailInput(
                attrs={'class':'form-control','placeholder':'Email'}
            ),
            'telefono': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Teléfono'}
            ),
            'rfc': forms.TextInput(
                attrs={'class':'form-control','placeholder':'RFC'}
            ),
            'tipo': forms.Select(
                attrs={'class':'form-control','placeholder':'Tipo'}
            ),
        }

class FormInstitucionEditar(FormInstitucion):
    class Meta:
        exclude = ['clave']
        model = Institucion

class FiltrosInstitucion(FormInstitucion):
    
    def __init__(self, *args, **kwargs):
        super(FiltrosInstitucion, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].required = False


#forms programas---------------------------

class FormProgramaAcademico(forms.ModelForm):
    
    class Meta:
        model = ProgramaAcademico
        fields = '__all__'
        # fields = ['clave, nombre']



class FormProgramaAcademico(forms.ModelForm):
    
    class Meta:
        model = ProgramaAcademico
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Nombre'}
            ),
            'latitud': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Latitud'}
            ),
            'longitud': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Longitud'}
            ),
            'telefono': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Teléfono'}
            ),
            'unidad_academica': forms.Select(
                attrs={'class':'form-control','placeholder':'Unidad Académica'}
            ),
        }

class FormProgramaAcademicoEditar(FormProgramaAcademico):
    class Meta:
        exclude = ['clave']
        model = ProgramaAcademico

class FiltrosProgramaAcademico(FormProgramaAcademico):
    
    def __init__(self, *args, **kwargs):
        super(FiltrosProgramaAcademico, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].required = False

#forms unidades----------------------------------------

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