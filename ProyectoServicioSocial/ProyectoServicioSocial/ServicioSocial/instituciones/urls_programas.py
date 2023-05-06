from django.urls import path
from instituciones import views


urlpatterns = [
    #path('', views.ListaProgramas.as_view(), name='lista_programas'),
    path('', views.ListaProgramas.as_view(), name='lista_programas'),
    path('nuevo', views.NuevaPrograma.as_view(), name='nuevo_programa'),
    path('eliminar/<str:pk>', views.EliminarPrograma.as_view(), name='eliminar_programa'),
    path('editar/<str:pk>', views.EditarPrograma.as_view(), name='editar_programa'),
    
]