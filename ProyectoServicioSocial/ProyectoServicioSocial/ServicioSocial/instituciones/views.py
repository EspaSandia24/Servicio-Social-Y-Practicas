from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from instituciones.models import ProgramaAcademico
from instituciones.forms import FormProgramaAcademico
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import ProgramaAcademico, UnidadAcademica, Institucion
from .forms import FormProgramaAcademico, FormProgramaAcademicoEditar, FiltrosProgramaAcademico, FormUnidadAcademica, FormUnidadAcademicaEditar, FiltrosUnidadAcademica
from .forms import FormInstitucion, FormInstitucionEditar, FiltrosInstitucion
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


#instituciones------------------

class ListaInstituciones(LoginRequiredMixin, ListView):
    template_name = 'instituciones_templates/institucion_list.html'
    paginate_by = 3
    model = Institucion
    extra_context = {'form': FiltrosInstitucion}
    page_kwarg = 'page'

class NuevaInstitucion(LoginRequiredMixin, CreateView):
    template_name = 'instituciones_templates/institucion_form.html'
    model = Institucion
    form_class = FormInstitucion
    # fields = '__all__'
    success_url = reverse_lazy('lista_instituciones')
    extra_context = {'accion': 'Nueva'}

class EditarInstitucion(LoginRequiredMixin, UpdateView):
    template_name = 'instituciones_templates/institucion_form.html'
    model = Institucion
    form_class = FormInstitucionEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_instituciones')

class EliminarInstitucion(LoginRequiredMixin, DeleteView):
    template_name = 'instituciones_templates/institucion_confirm_delete.html'
    model = Institucion
    success_url = reverse_lazy('lista_instituciones')

#programas-------------------

class ListaProgramas(LoginRequiredMixin, ListView):
    template_name = 'programas_academicas/programaacademico_list.html'
    paginate_by = 3
    model = ProgramaAcademico
    extra_context = {'form': FiltrosProgramaAcademico}
    page_kwarg = 'page'  

    
class NuevaPrograma(LoginRequiredMixin, CreateView):
    template_name = 'programas_academicas/programaacademico_form.html'
    model = ProgramaAcademico
    form_class = FormProgramaAcademico
    # fields = '__all__'
    success_url = reverse_lazy('lista_programas')
    extra_context = {'accion': 'Nueva'}
    
    
class EditarPrograma(LoginRequiredMixin, UpdateView):
    template_name = 'programas_academicas/programaacademico_form.html'
    model = ProgramaAcademico
    form_class = FormProgramaAcademicoEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_programas')

class EliminarPrograma(LoginRequiredMixin, DeleteView):
    template_name = 'programas_academicas/programaacademico_confirm_delete.html'
    model = ProgramaAcademico
    success_url = reverse_lazy('lista_programas')




#unidades------------
class NuevaUnidad(LoginRequiredMixin, CreateView):
    template_name = 'unidades_academicas/unidadacademica_form.html'
    model = UnidadAcademica
    form_class = FormUnidadAcademica
    # fields = '__all__'
    success_url = reverse_lazy('lista_unidades')
    extra_context = {'accion': 'Nueva'}

    
class EditarUnidad(LoginRequiredMixin, UpdateView):
    template_name = 'unidades_academicas/unidadacademica_form.html'
    model = UnidadAcademica
    form_class = FormUnidadAcademicaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_unidades')

class EliminarUnidad(LoginRequiredMixin, DeleteView):
    template_name = 'unidades_academicas/unidadacademica_confirm_delete.html'
    model = UnidadAcademica
    success_url = reverse_lazy('lista_unidades')

class ListaUnidades(LoginRequiredMixin, ListView):
    template_name = 'unidades_academicas/unidadacademica_list.html'
    paginate_by = 3
    model = UnidadAcademica
    extra_context = {'form': FiltrosUnidadAcademica}
    page_kwarg = 'page'  # add this attribute to specify the page parameter name


#--------------
