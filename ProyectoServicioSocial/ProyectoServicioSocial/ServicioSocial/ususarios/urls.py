from django.urls import path
from ususarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.PaginaInicio.as_view(), name='bienvenida'),
    path('salir', LogoutView.as_view(), name='logout'),
    path('entrar', views.LoginView.as_view(), name='login'),
    path('registrar', views.RegistrarView.as_view(), name='registrar'),
    path('perfil', views.CrearPerfilView.as_view(), name='perfil'),
]