from django import forms
from .models import ReporteInicial, TIPO, ReporteMensual

class FormReporteI(forms.ModelForm):
    
    class Meta:
        model = ReporteInicial
        # exclude = ['optativa']
        fields = '__all__'
        
        widgets = {
            'mes1': forms.TextInput(
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
                attrs={'class':'form-control','placeholder':'Actividades',"required": False}
            ),'mes7': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades',"required": False}
            ),'mes8': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades',"required": False}
            ),'mes9': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades',"required": False}
            ),'mes10': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades',"required": False}
            ),'mes11': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades',"required": False}
            ),'mes12': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades',"required": False}
            ),'tipo': forms.Select(
                attrs={'class':'form-control','placeholder':'Tipo'}
            ),  
        }

class FormReporteIEditar(FormReporteI):
    class Meta:
        exclude = ['id']
        model = ReporteInicial
        
#-------------------

class FormReporteM(forms.ModelForm):
    
    class Meta:
        model = ReporteMensual
        # exclude = ['optativa']
        fields = '__all__'
        
        widgets = {
            'Alumno': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Alumno'}
            ),
            'actividades': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'horas': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Horas Reportadas'}
            ),'tipo': forms.Select(
                attrs={'class':'form-control','placeholder':'Tipo'}
            ),'fecha_inicio': forms.DateInput(
                attrs={'class':'form-control','placeholder':'DD/MM/AA'}
            ),'fecha_termino': forms.DateInput(
                attrs={'class':'form-control','placeholder':'DD/MM/AA'}
            ),'fecha': forms.DateInput(
                attrs={'class':'form-control','placeholder':'DD/MM/AA'}
            ),
            
        }

class FormReporteMEditar(FormReporteM):
    class Meta:
        exclude = ['id']
        model = ReporteMensual