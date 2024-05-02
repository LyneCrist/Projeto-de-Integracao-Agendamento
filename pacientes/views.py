from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Paciente
from .forms import PacienteForm
from django.contrib import messages


def listar(request):

    context = {}

    # context["pacientes"] = Paciente.objects.all()[:15].order_by(
    #     "data_criacao, data_alteracao"
    # )

    context["pacientes"] = Paciente.objects.all()[:15]

    return render(request, "lista_pacientes.html", context)


def cadastrar(request):

    context = {}

    context["title"] = "Cadastro de Paciente"

    if request.method == "POST":

        context["form"] = PacienteForm(request.POST)

        if context["form"].is_valid():
            try:

                # print(context["form"].cleaned_data)

                context["form"].save()

                messages.success(request, "Paciente cadastrado com sucesso")

                return redirect("cadastra_paciente")

            except:

                messages.error(
                    request, "Ocorreu um erro durante o registo, tente novamente"
                )

                return render(request, "formulario_paciente.html", context)

        context["erros"] = context["form"].errors.as_data()

    else:
        context["form"] = PacienteForm()

    return render(request, "formulario_paciente.html", context)


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
