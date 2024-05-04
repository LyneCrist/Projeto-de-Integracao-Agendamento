from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="lista_pacientes"),
    path("cadastro/", views.cadastrar, name="criar_paciente"),
    path("edita/<int:id>", views.atualizar, name="edita_paciente"),
    path("exclui/<int:id>", views.excluir, name="exclui_paciente"),
]
