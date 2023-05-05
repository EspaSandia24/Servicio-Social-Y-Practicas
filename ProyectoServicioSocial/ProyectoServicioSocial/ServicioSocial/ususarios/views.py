from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
