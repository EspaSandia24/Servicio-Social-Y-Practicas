from django import forms
from .models import ReporteInicial, TIPO, ReporteMensual, EvaluacionFinal

class FormReporteI(forms.ModelForm):
    
    class Meta:
        model = ReporteInicial
        # exclude = ['optativa']
        fields = '__all__'
        
        widgets = {
            'alumno': forms.Select(
                attrs={'class':'form-control','placeholder':'Alumno'}),
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
            'fecha': forms.DateInput(
                attrs={'class':'form-control','placeholder':'dd/mm/aaaa',"required": True}
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
            'alumno': forms.Select(
                attrs={'class':'form-control','placeholder':'Alumno'}
            ),'actividades': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Actividades'}
            ),'horas_Reportadas': forms.TextInput(
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

#-------------------------------

class FormEvaluacionFinal(forms.ModelForm):
    
    class Meta:
        model = EvaluacionFinal
        fields = '__all__'
        
        widgets = {
            'alumno': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Alumno'}
            ),
            'fecha_inicio': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}
            ),
            'fecha_termino': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'DD/MM/AA'}
            ),
            'institucion': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Institución'}
            ),
            'puntualidad': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Puntuación para la puntualidad'}
            ),
            'cumplimiento_actividades': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Puntuación para el cumplimiento de actividades'}
            ),
            'actividades_ordenadas': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Puntuación para la realización ordenada de actividades'}
            ),
            'conocimientos_suficientes': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Puntuación para los conocimientos suficientes'}
            ),
            'comportamiento': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Puntuación para el comportamiento'}
            ),
            'actitud': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Puntuación para la actitud'}
            ),
            'actitud_actividad_desconocida': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Actitud ante una actividad desconocida'}
            ),
            'calificacion': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Calificación'}
            ),
            'observaciones': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Observaciones'}
            ),
        }

class FormEvaluacionFinalEditar(FormEvaluacionFinal):
    class Meta:
        exclude = ['id']
        model = EvaluacionFinal