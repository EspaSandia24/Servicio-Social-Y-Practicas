from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

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
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
