from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import UserForm, FormDatosPersonales
from .models import DatosPersonales
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PaginaInicio(LoginRequiredMixin, TemplateView):
    template_name = 'bienvenida.html'

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

class RegistrarView(SuccessMessageMixin, CreateView):
    template_name = 'user_form.html'
    moddel = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = "%(username)s se registró con éxito."

class CrearPerfilView(SuccessMessageMixin, CreateView):
    # template_name = 'bienvenida.html'
    model = DatosPersonales
    form_class = FormDatosPersonales
    success_url = reverse_lazy('bienvenida')
    success_message = "Se guardaron tus datos personales correctamente."

    def form_valid(self, form):
        datos_personales = form.save(commit=False)
        datos_personales.user(self.request.user)
        datos_personales.save()

        return super().form_valid(form)