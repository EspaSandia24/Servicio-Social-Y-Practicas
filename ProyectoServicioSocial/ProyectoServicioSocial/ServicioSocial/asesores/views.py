from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Asesores
from .forms import FiltrosAsesores, FormAsesores, FormAsesoresEditar
from django.contrib.auth.mixins import LoginRequiredMixin


class AsesoresList(LoginRequiredMixin, ListView):
    template_name = 'asesores_list.html'
    paginate_by = 3
    model = Asesores
    page_kwarg = 'page'

class NuevoAsesor(LoginRequiredMixin, CreateView):
    template_name = 'asesores_form.html'
    model = Asesores
    form_class = FormAsesores
    success_url = reverse_lazy('lista_asesores')
    extra_context = {'accion': 'Nuevo'}
    
class EditarAsesor(LoginRequiredMixin, UpdateView):
    template_name = 'asesores_form.html'
    model = Asesores
    form_class = FormAsesoresEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_asesores')

class EliminarAsesor(LoginRequiredMixin, DeleteView):
    template_name = 'asesores_confirm_delete.html'
    model = Asesores
    success_url = reverse_lazy('lista_asesores')