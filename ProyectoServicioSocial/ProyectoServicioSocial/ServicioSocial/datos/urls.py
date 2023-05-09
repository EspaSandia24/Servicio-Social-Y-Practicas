from django.urls import path
from datos import views

urlpatterns = [
    path('', views.DatosList.as_view(), name='lista_alumnos'),
    path('nuevos_datos', views.NuevosDatos.as_view(), name='nuevos_datos'),
    path('editar/<str:pk>', views.EditarDatos.as_view(), name='editar_datos'),
    path('eliminar/<str:pk>', views.EliminarDatos.as_view(), name='eliminar_datos'),
    
    
]