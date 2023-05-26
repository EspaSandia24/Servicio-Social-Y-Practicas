from django.urls import path
from reportes import views

urlpatterns = [
    path('', views.ListaEvalFin.as_view(), name='lista_evaluaciones_finales'),
    path('nuevo', views.NuevoEvalFin.as_view(), name='nuevo_evaluacion_final'),
    path('editar/<str:pk>', views.EditarEvalFin.as_view(), name='editar_evaluacion_final'),
    path('eliminar/<str:pk>', views.EliminarEvalFin.as_view(), name='eliminar_evaluacion_final'),
]
