from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from instituciones.models import ProgramaAcademico
from instituciones.forms import FormProgramaAcademico
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import ProgramaAcademico, UnidadAcademica
from .forms import FormProgramaAcademico, FormUnidadAcademica, FormUnidadAcademicaEditar, FiltrosUnidadAcademica



# Create your views here.
#unidades------------
class NuevaUnidad(CreateView):
    template_name = 'unidades_academicas/unidadacademica_form.html'
    model = UnidadAcademica
    form_class = FormUnidadAcademica
    # fields = '__all__'
    success_url = reverse_lazy('lista_unidades')
    extra_context = {'accion': 'Nueva'}

    
class EditarUnidad(UpdateView):
    template_name = 'unidades_academicas/unidadacademica_form.html'
    model = UnidadAcademica
    form_class = FormUnidadAcademicaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_unidades')

class EliminarUnidad(DeleteView):
    template_name = 'unidades_academicas/unidadacademica_confirm_delete.html'
    model = UnidadAcademica
    success_url = reverse_lazy('lista_unidades')

class ListaUnidades(ListView):
    template_name = 'unidades_academicas/unidadacademica_list.html'
    paginate_by = 5
    model = UnidadAcademica
    extra_context = {'form': FiltrosUnidadAcademica}
    page_kwarg = 'page'  # add this attribute to specify the page parameter name


#--------------
#programas e instituciones en progreso
def lista_programas(request):
    programas = "a"
    
    return None