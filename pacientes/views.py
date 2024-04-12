from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import PacienteForm


def listar(request):
    return render(request, "lista_pacientes.html")


def cadastrar(request):

    print(type(request))

    # if request.method == "POST":

    #     # "nome"
    #     # "sobreNome"
    #     # "email"
    #     # "telefone"
    #     # "senha"
    #     # "confirmaSenha"
    #     # "genero"

    #     form = PacienteForm(request.POST)

    #     if form.is_valid():

    #         return HttpResponseRedirect("/thanks/")

    # form = PacienteForm()

    return render(request, "formulario_paciente.html", {"form": ""})


def atualizar(request):
    return render(request, "formulario_paciente.html")


def excluir(request):
    return render(request, "lista_pacientes.html")
