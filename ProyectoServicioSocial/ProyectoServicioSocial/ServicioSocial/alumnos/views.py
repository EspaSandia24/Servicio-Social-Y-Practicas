from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Alumnos
from .forms import FiltrosAlumnos, FormAlumnos, FormAlumnosEditar
from django.contrib.auth.mixins import LoginRequiredMixin

class PaginaInicio(LoginRequiredMixin, TemplateView):
    template_name = 'bienvenida.html'

class AlumnosList(LoginRequiredMixin, ListView):
    template_name = 'alumnos_list.html'
    paginate_by = 3
    model = Alumnos
    extra_context = {'form': FiltrosAlumnos}
    page_kwarg = 'page'

class NuevoAlumno(LoginRequiredMixin, CreateView):
    template_name = 'alumnos_form.html'
    model = Alumnos
    form_class = FormAlumnos
    # fields = '__all__'
    success_url = reverse_lazy('lista_alumnos')
    extra_context = {'accion': 'Nuevo'}
    
class EditarAlumno(LoginRequiredMixin, UpdateView):
    template_name = 'alumnos_form.html'
    model = Alumnos
    form_class = FormAlumnosEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_alumnos')

class EliminarAlumno(LoginRequiredMixin, DeleteView):
    template_name = 'alumnos_confirm_delete.html'
    model = Alumnos
    success_url = reverse_lazy('lista_alumnos')