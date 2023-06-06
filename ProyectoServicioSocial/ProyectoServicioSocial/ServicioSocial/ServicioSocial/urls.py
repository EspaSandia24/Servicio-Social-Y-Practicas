from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from ususarios.views import Bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ususarios/', include('ususarios.urls')),
    path('programas/', include('instituciones.urls_programas')),
    path('unidades/', include('instituciones.urls_unidades')),
    path('reportes_iniciales/', include('reportes.urls_reporteI')),
    path('instituciones/', include('instituciones.urls_instituciones')),
    path('alumnos/', include('alumnos.urls')),
    path('reportes_mensuales/', include('reportes.urls_reporteM')),
    path('datos/', include('datos.urls')),
    path('', Bienvenida.as_view(), name='bienvenida'),
    path('reportes_eval_fin/', include('reportes.urls_reporteEvalFinal')),
    path('reportes_finales/', include('reportes.urls_reporteF')),
    path('grafica/', include('reportes.urls_graficas')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
