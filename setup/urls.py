from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/consultas/")),
    path("consultas/", include("consultas.urls")),
    path("enderecos/", include("enderecos.urls")),
    path("pacientes/", include("pacientes.urls")),
    path("auth/", include("usuarios.urls")),
]
