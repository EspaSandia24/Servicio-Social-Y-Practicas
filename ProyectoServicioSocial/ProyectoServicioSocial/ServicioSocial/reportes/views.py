from django.shortcuts import render , redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ReporteInicial
from django.urls import reverse_lazy
from .forms import FormReporteI, FormReporteIEditar

class ListaReportes(ListView):
    template_name ='reporteinicial_list.html'
    paginate_by = 2
    model = ReporteInicial
    
class NuevoReporteI(CreateView):
    template_name ='reporteinicial_form.html'
    model = ReporteInicial
    #form_class = FormMateria
    fields = '__all__'
    success_url = reverse_lazy('lista_reporteI')
    extra_context = {'accion': 'Nuevo'}
    
    # template_name = 'alta_materia.html'
    # fields = ['nombre','clave','semestre']
    
class EditarReporteI(UpdateView):
    template_name ='reporteinicial_form.html'
    model = ReporteInicial
    form_class = FormReporteIEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_reporteI')
    
class EliminarReporteI(DeleteView):
    template_name ='reporteinicial_comfirm_delete.html'
    model = ReporteInicial
    success_url = reverse_lazy('lista_reporteI')
