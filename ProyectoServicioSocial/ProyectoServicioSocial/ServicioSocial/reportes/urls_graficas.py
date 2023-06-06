from django.urls import path
from reportes import views

urlpatterns = [
    path('', views.grafica_alumnos, name='grafica'),
]
