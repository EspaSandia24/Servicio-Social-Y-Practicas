from django.urls import path
from instituciones import views

urlpatterns = [
    path('', views.ListaInstituciones.as_view(), name='lista_instituciones'),
    path('nuevo', views.NuevaInstitucion.as_view(), name='nuevo_institucion'),
    path('eliminar/<str:pk>', views.EliminarInstitucion.as_view(), name='eliminar_institucion'),
    path('editar/<str:pk>', views.EditarInstitucion.as_view(), name='editar_institucion'),
    
]