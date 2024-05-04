from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Paciente
from .forms import PacienteForm
from django.contrib import messages


def listar(request):

    context = {}

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

                return redirect("criar_paciente")

            except:

                messages.error(
                    request, "Ocorreu um erro durante o registo, tente novamente"
                )

                return render(request, "criar_paciente.html", context)

        context["erros"] = context["form"].errors.as_data()

    else:
        context["form"] = PacienteForm()

    return render(request, "criar_paciente.html", context)


def atualizar(request, pk: int):

    context = {}

    paciente = Paciente.objects.get(pk=pk)

    if request.method == "POST":

        context["form"] = PacienteForm(request.POST, instance=paciente)

        if context["form"].is_valid():

            # print(context["form"].cleaned_data)
            context["form"].save()

            return redirect("paciente-detail", paciente.pk)
    else:
        context["form"] = PacienteForm(instance=paciente)

    return render(request, "editar_paciente.html", context)


def excluir(request, pk: int):

    if request.method == "POST":

        paciente = Paciente.objects.get(id=pk)
        paciente.delete()

    return redirect("/lista_pacientes/")
