from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('usuarios.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('locais/', include('locais.urls')),
    path('agendamentos/', include('agendamentos.urls')),
]
