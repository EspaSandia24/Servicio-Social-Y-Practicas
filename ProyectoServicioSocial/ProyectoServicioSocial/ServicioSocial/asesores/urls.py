from django.urls import path
from asesores import views

urlpatterns = [
    path('', views.AsesoresList.as_view(), name='lista_asesores'),
    path('nuevo_asesor', views.NuevoAsesor.as_view(), name='nuevo_asesor'),
    path('editar/<str:pk>', views.EditarAsesor.as_view(), name='editar_asesor'),
    path('eliminar/<str:pk>', views.EliminarAsesor.as_view(), name='eliminar_asesor'),
    
    
]