from django.urls import path
from instituciones import views

urlpatterns = [
    path('', views.ListaUnidades.as_view(), name='lista_unidades'),
    #path('list', views.lista_programas, name='lista_programas2'),
    path('nuevo', views.NuevaUnidad.as_view(), name='nuevo_unidad'),
    path('eliminar/<int:pk>', views.EliminarUnidad.as_view(), name='eliminar_unidad'),
    path('editar/<int:pk>', views.EditarUnidad.as_view(), name='editar_unidad'),
    
]