from django.shortcuts import render , redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ReporteInicial, ReporteMensual
from django.urls import reverse_lazy
from .forms import FormReporteIEditar,FormReporteMEditar

class ListaReportesI(ListView):
    template_name ='reporteinicial_list.html'
    paginate_by = 2
    model = ReporteInicial
    
class NuevoReporteI(CreateView):
    template_name ='reporteinicial_form.html'
    model = ReporteInicial
    #form_class = FormMateria
    fields = '__all__'
    success_url = reverse_lazy('lista_reportesI')
    extra_context = {'accion': 'Nuevo'}
    
    # template_name = 'alta_materia.html'
    # fields = ['nombre','clave','semestre']
    
class EditarReporteI(UpdateView):
    template_name ='reporteinicial_form.html'
    model = ReporteInicial
    form_class = FormReporteIEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_reportesI')
    
class EliminarReporteI(DeleteView):
    template_name ='reporteinicial_confirm_delete.html'
    model = ReporteInicial
    success_url = reverse_lazy('lista_reportesI')

#----------------------------------------------------------

class ListaReportesM(ListView):
    template_name ='reportemensual_list.html'
    paginate_by = 2
    model = ReporteMensual
    
class NuevoReporteM(CreateView):
    template_name ='reportemensual_form.html'
    model = ReporteMensual
    fields = '__all__'
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