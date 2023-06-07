from django.shortcuts import render , redirect
from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ReporteInicial, ReporteMensual, EvaluacionFinal, Reporte_Final
from instituciones.models import ProgramaAcademico
from alumnos.models import Alumnos
from django.urls import reverse_lazy
from .forms import FormReporteIEditar,FormReporteMEditar,FormReporteI,FormReporteM,FormEvaluacionFinal, FromReporteFinal,FormReporteFEditar
from django.http import HttpResponse
from reportes.utils import render_to_pdf


class ListaReportesI(LoginRequiredMixin, ListView):

    template_name ='reporteinicial_list.html'
    model = ReporteInicial
    
class NuevoReporteI(LoginRequiredMixin, CreateView):
    template_name ='reporteinicial_form.html'
    model = ReporteInicial
    form_class = FormReporteI
    success_url = reverse_lazy('lista_reportesI')
    extra_context = {'accion': 'Nuevo'}
 
    
class EditarReporteI(LoginRequiredMixin, UpdateView):
    template_name ='reporteinicial_form.html'
    model = ReporteInicial
    form_class = FormReporteIEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_reportesI')
    


class EliminarReporteI(LoginRequiredMixin, DeleteView):
    template_name ='reporteinicial_confirm_delete.html'

    model = ReporteInicial
    success_url = reverse_lazy('lista_reportesI')


class GenerarPdfInicial(View):
    def get(self, request, *args, **kwargs):
        model = ReporteInicial
        # reportes = ReporteInicial.objects.all()
        data = {
            'alumno' : model.alumno,
            'mes1' : model.mes1,
            'mes2' : model.mes2,
            'mes3' : model.mes3,
            'mes4' : model.mes4,
            'mes5' : model.mes5,
            'mes6' : model.mes6,
            'mes7' : model.mes7,
            'mes8' : model.mes8,
        }
        pdf = render_to_pdf('generarPdfInicial.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

#----------------------------------------------------------

class ListaReportesM(ListView):
    template_name ='reportemensual_list.html'
    paginate_by = 2
    model = ReporteMensual
    
class NuevoReporteM(CreateView):
    template_name ='reportemensual_form.html'
    model = ReporteMensual
    form_class = FormReporteM
    success_url = reverse_lazy('lista_reportesM')
    extra_context = {'accion': 'Nuevo'}
    
class EditarReporteM(UpdateView):
    template_name ='reportemensual_form.html'
    model = ReporteMensual
    form_class = FormReporteMEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_reportesM')
    
class EliminarReporteM(DeleteView):
    template_name ='reportemensual_confirm_delete.html'
    model = ReporteMensual
    success_url = reverse_lazy('lista_reportesM')

class GenerarPdfMensual(View):
    def get(self, request, *args, **kwargs):
        model = ReporteMensual
        # reportes = ReporteInicial.objects.all()
        data = {
            'alumno' : model.alumno,
            'tipo' : model.tipo,
        }
        pdf = render_to_pdf('generarPdfMensual.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

#-------------------------
class ListaEvalFin(ListView):
    template_name ='reporteEvalFinal_list.html'
    paginate_by = 2
    model = EvaluacionFinal
    
class NuevoEvalFin(CreateView):
    template_name ='reporteEvalFinal_form.html'
    model = EvaluacionFinal
    form_class = FormEvaluacionFinal
    success_url = reverse_lazy('lista_evaluaciones_finales')
    extra_context = {'accion': 'Nuevo'}
    
class EditarEvalFin(UpdateView):
    template_name ='reporteEvalFinal_form.html'
    model = EvaluacionFinal
    form_class = FormReporteMEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_evaluaciones_finales')
    
class EliminarEvalFin(DeleteView):
    template_name ='reporteEvalFin_confirm_delete.html'
    model = EvaluacionFinal
    success_url = reverse_lazy('lista_evaluaciones_finales')
    
#-------------------------------------------------
class ListaReportesF(LoginRequiredMixin, ListView):

    template_name ='reportefinal_list.html'
    model = Reporte_Final
    
class NuevoReporteF(LoginRequiredMixin, CreateView):
    template_name ='reportefinal_form.html'
    model = Reporte_Final
    form_class = FromReporteFinal
    success_url = reverse_lazy('lista_reportesF')
    extra_context = {'accion': 'Nuevo'}
 
    
class EditarReporteF(LoginRequiredMixin, UpdateView):
    template_name ='reportefinal_form.html'
    model = Reporte_Final
    form_class = FormReporteFEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_reportesF')
    


class EliminarReporteF(LoginRequiredMixin, DeleteView):
    template_name ='reportefinal_confirm_delete.html'
    model = Reporte_Final
    success_url = reverse_lazy('lista_reportesF')

class GenerarPdfFinal(View):
    def get(self, request, *args, **kwargs):
        model = Reporte_Final
        # reportes = ReporteInicial.objects.all()
        data = {
            'alumno' : model.alumno,
        }
        pdf = render_to_pdf('generarPdfFinal.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

#-------------------------grafica
import json
from django.shortcuts import render
from .models import Alumnos
from instituciones.models import ProgramaAcademico

def grafica_alumnos(request):
    programas_academicos = ProgramaAcademico.objects.all()
    datos_grafica = []
    
    for programa in programas_academicos:
        cantidad_alumnos = Alumnos.objects.filter(programa_academico=programa).count()
        datos_grafica.append({
            'programa': programa.nombre,
            'alumnos': cantidad_alumnos
        })
    
    datos_grafica_json = json.dumps(datos_grafica)  # Convertir a JSON
    
    return render(request, 'grafica.html', {'datos_grafica': datos_grafica_json})

