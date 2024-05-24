from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="listar_transportes"),
    path(
        "paciente_transportes/<int:id>",
        views.paciente_transportes,
        name="paciente_transportes",
    ),
    path("cadastrar/<int:paciente_id>", views.cadastrar, name="criar_transporte"),
    path("editar/<int:id>", views.atualizar, name="editar_transporte"),
    path("excluir/<int:id>", views.excluir, name="excluir_transporte"),
    path("cancelar/<int:id>", views.cancelar, name="concelar_transporte"),
    path("finalizar/<int:id>", views.finalizar, name="finalizar_transporte"),
]
