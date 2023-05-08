from django.urls import path
from reportes import views

urlpatterns = [
    path('', views.ListaReportesM.as_view(), name='lista_reportesM'),
    path('nuevoM', views.NuevoReporteM.as_view(), name='nuevo_reporteM'),
    path('editarM/<str:pk>', views.EditarReporteM.as_view(), name='editar_reporteM'),
    path('eliminarM/<str:pk>', views.EliminarReporteM.as_view(), name='eliminar_reporteM'),
]
