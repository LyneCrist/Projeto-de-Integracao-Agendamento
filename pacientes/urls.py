from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="lista_pacientes"),
    path("cadastro/", views.cadastrar, name="cadastra_paciente"),
    path("edita/", views.atualizar, name="edita_paciente"),
    path("exclui/", views.excluir, name="exclui_paciente"),
]
