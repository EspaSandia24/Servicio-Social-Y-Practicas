from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ususarios/', include('ususarios.urls')),
    path('programas/', include('instituciones.urls_programas')),
    path('unidades/', include('instituciones.urls_unidades')),
    path('reportes/', include('reportes.urls')),
    path('instituciones/', include('instituciones.urls_instituciones')),
    path('alumnos/', include('alumnos.urls')),
    
]
