from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.lista_pacientes, name="lista_pacientes"),
    path('cadastro/', views.cadastro, name="cadastro_paciente"),
]
