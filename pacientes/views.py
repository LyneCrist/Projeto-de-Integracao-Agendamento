from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Paciente
from .forms import PacienteForm


def listar(request):
    return render(request, "lista_pacientes.html")


def cadastrar(request):

    # form = PacienteForm()

    # paciente = Paciente.objects.all()

    # context = {"paciente": paciente, "title": "Cadastro de Paciente", "form": form}

    # return render(request, "formulario_paciente", context)

    context = {}

    context["form"] = PacienteForm()
    context["title"] = "Cadastro de Paciente"

    if request.method == "POST":

        form = PacienteForm(request.POST)

        if form.is_valid():
            try:
                # form.save()
                print(form.cleaned_data)

                return redirect("/lista_pacientes/")
            except:
                return render(request, "formulario_paciente", context)
        else:
            context["erros"] = form.errors

    return render(request, "formulario_paciente", context)

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


def atualizar(request, pk: int):

    if request.method == "POST":

        paciente = Paciente.objects.get(id=pk)

        form = PacienteForm(instance=paciente)

    return redirect("/lista_pacientes/")


def excluir(request, pk: int):

    if request.method == "POST":

        paciente = Paciente.objects.get(id=pk)
        paciente.delete()

    return redirect("/lista_pacientes/")
