from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Datos
from .forms import FiltrosDatos, FormDatos, FormDatosEditar

class DatosList(ListView):
    template_name = 'datos_list.html'
    paginate_by = 3
    model = Datos
    extra_context = {'form': FiltrosDatos}
    page_kwarg = 'page'
    

class NuevosDatos(CreateView):
    template_name = 'datos_form.html'
    model = Datos
    form_class = FormDatos
    # fields = '__all__'
    success_url = reverse_lazy('lista_datos')
    extra_context = {'accion': 'Nuevo'}
    
    
class EditarDatos(UpdateView):
    template_name = 'datos_form.html'
    model = Datos
    form_class = FormDatosEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_datos')

class EliminarDatos(DeleteView):
    template_name = 'datos_confirm_delete.html'
    model = Datos
    success_url = reverse_lazy('lista_datos')