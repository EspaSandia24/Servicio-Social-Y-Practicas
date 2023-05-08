from django import forms
from .models import ReporteInicial, TIPO

class FormReporteI(forms.ModelForm):
    
    class Meta:
        model = ReporteInicial
        # exclude = ['optativa']
        fields = '__all__'
        
        widgets = {
            'mes1': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes1': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes2': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes3': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes4': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes5': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes6': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes7': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes8': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes9': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes10': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes11': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'mes12': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'tipo': forms.Select(
                attrs={'class':'form-control','placeholder':'Tipo'}
            ),
            
        }

class FormReporteIEditar(FormReporteI):
    class Meta:
        exclude = ['id']
        model = ReporteInicial