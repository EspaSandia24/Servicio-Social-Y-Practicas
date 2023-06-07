from django.urls import path
from reportes import views

urlpatterns = [
    path('', views.ListaReportesI.as_view(), name='lista_reportesI'),
    path('nuevoI', views.NuevoReporteI.as_view(), name='nuevo_reporteI'),
    path('editarI/<str:pk>', views.EditarReporteI.as_view(), name='editar_reporteI'),
    path('eliminarI/<str:pk>', views.EliminarReporteI.as_view(), name='eliminar_reporteI'),
    path('pdfInicial', views.GenerarPdfInicial.as_view(), name='pdf_inicial'),
]
