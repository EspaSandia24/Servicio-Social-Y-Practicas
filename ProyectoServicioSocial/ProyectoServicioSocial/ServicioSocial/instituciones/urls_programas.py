from django.urls import path
from instituciones import views

urlpatterns = [
    path('', views.lista_programas, name='lista_programas'),
]