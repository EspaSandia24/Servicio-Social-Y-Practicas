from django.urls import path
from reportes import views

urlpatterns = [
    path('', views.ListaReportesF.as_view(), name='lista_reportesF'),
    path('nuevoF', views.NuevoReporteF.as_view(), name='nuevo_reporteF'),
    path('editarF/<str:pk>', views.EditarReporteF.as_view(), name='editar_reporteF'),
    path('eliminarF/<str:pk>', views.EliminarReporteF.as_view(), name='eliminar_reporteF'),
]
