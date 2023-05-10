from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from .token import token_activation
from .forms import UserForm, FormDatosPersonales
from .models import DatosPersonales

class PaginaInicio(LoginRequiredMixin, TemplateView):
    template_name = 'bienvenida.html'

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

class ActivarCuentaView(TemplateView):
    def get(self, request, *args, **kwargs):

        try: 
            uid = urlsafe_base64_decode(kwargs['uidb64'])
            token = kwargs['token']
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, User.DoesNotExist):
            user = None

        if user is not None and token_activation.check_token(user, token):
            user.is_active = True
            user.save()

            messages.success(request, 'Cuenta activada, ingresar datos.')
        else:
            messages.error(request, 'Token inválido, contacta al administrador.')

        return redirect('login')

class RegistrarView(SuccessMessageMixin, CreateView):
    template_name = 'user_form.html'
    moddel = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = "%(username)s se registró con éxito."

    def form_valid(self, form):
        form = UserForm(self.request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            sitio = get_current_site(self.request)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = token_activation.make_token(user)

            mensaje = render_to_string(
                'confirmar_cuenta.html',
                {
                    'user': user,
                    'sitio': sitio,
                    'uid': uid,
                    'token': token
                }
            )
            asunto = 'Activar cuenta'
            para = user.email
            email = EmailMessage(
                asunto,
                mensaje,
                to=[para],
            )
            email.content_subtype = 'html'
            email.send()
        else: 
            return self.render_to_response(self.get_context_data(form=form))

        return super().form_valid(form)

class CrearPerfilView(SuccessMessageMixin, CreateView):
    # template_name = 'bienvenida.html'
    model = DatosPersonales
    form_class = FormDatosPersonales
    success_url = reverse_lazy('bienvenida')
    success_message = "Se guardaron tus datos personales correctamente."

    def form_valid(self, form):
        datos_personales = form.save(commit=False)
        datos_personales.user = self.request.user
        datos_personales.save()

        return super().form_valid(form)
    

class ListaUsuariosView(ListView):
    model = User
    template_name = 'lista_usuarios.html'

    def get_context_data(self, **kwargs):
        context = super(ListaUsuariosView, self).get_context_data(**kwargs)
        context['grupos'] = Group.objects.all()
        return context


def asignar_grupos(request):
    print(request.POST)
    id_usuario = request.POST.get('usuario', None)
    usuario = User.objects.get(id=id_usuario)

    usuario.groups.clear()
    for item in request.POST:
        if request.POST[item] == 'on':
            grupo = Group.objects.get(id=int(item))
            usuario.groups.add(grupo)

    messages.success(request, 'Se agregó el usuario al grupo.')

    return redirect('lista')