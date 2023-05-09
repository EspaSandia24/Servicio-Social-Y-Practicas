from django.urls import path
from alumnos import views

urlpatterns = [
    path('', views.PaginaInicio.as_view(), name='bienvenida'),
    path('lista_alumnos', views.AlumnosList.as_view(), name='lista_alumnos'),
    path('nuevo_alumno', views.NuevoAlumno.as_view(), name='nuevo_alumno'),
    path('eliminar/<str:pk>', views.EliminarAlumno.as_view(), name='eliminar_alumno'),
    path('editar/<str:pk>', views.EditarAlumno.as_view(), name='editar_alumno'),
    
]