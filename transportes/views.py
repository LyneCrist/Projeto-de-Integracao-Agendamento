from django.shortcuts import render, redirect

from .forms import TransporteForm
from .models import Transporte
from pacientes.models import Paciente

from django.contrib import messages


def listar(request):

    context = {}

    context["transportes"] = Transporte.objects.all()

    return render(request, "lista_transportes.html", context)


def paciente_transportes(request, id: int):

    context = {}

    paciente: Paciente = Paciente.objects.get(id=id)

    transportes = Transporte.objects.filter(paciente=paciente)

    context["nome"] = paciente.nome

    context["transportes"] = transportes

    return render(request, "paciente_transportes.html", context)


def cadastrar(request, paciente_id: int):

    paciente: Paciente = Paciente.objects.get(id=paciente_id)

    context = {}

    context["title"] = "Cadastra Transporte"
    context["paciente_id"] = paciente.pk
    context["nome"] = paciente.nome
    context["cod_sus"] = paciente.cartao_sus

    if request.method == "POST":

        context["form"] = TransporteForm(request.POST)

        if context["form"].is_valid():
            try:

                # print(context["form"].cleaned_data)

                novo_transporte: Transporte = context["form"].save(commit=False)

                novo_transporte.paciente = paciente

                novo_transporte.save()

                # messages.success(request, "Transporte cadastrado com sucesso")

                # return redirect("listar_por_paciente", paciente_id=paciente.pk)
                return redirect("listar_pacientes")

            except Exception as exc:

                messages.error(
                    request, "Ocorreu um erro durante o registro, tente novamente"
                )

                return render(request, "criar_transporte.html", context)

        context["errors"] = context["form"].errors.as_data()

    else:
        context["form"] = TransporteForm()

    return render(request, "criar_transporte.html", context)


def atualizar(request, id: int):

    context = {}

    transporte = Transporte.objects.get(id=id)

    if request.method == "POST":

        context["form"] = TransporteForm(request.POST, instance=transporte)

        if context["form"].is_valid():

            context["form"].save()

            return redirect("editar_condicao", transporte.pk)

        context["erros"] = context["form"].errors.as_data()

        print(context["erros"])

    context["id"] = transporte.pk

    context["form"] = TransporteForm(instance=transporte)

    return render(request, "editar_transporte.html", context)


def excluir(request, id: int):

    # if request.method == "POST":

    transporte = Transporte.objects.get(id=id)
    transporte.delete()

    return redirect("listar_transportes")


def cancelar(request, id: int):

    # if request.method == "POST":

    # transporte = Transporte.objects.get(id=id)
    # transporte.delete()

    return redirect("concelar_transporte")


def finalizar(request, id: int):

    # if request.method == "POST":

    # transporte = Transporte.objects.get(id=id)
    # transporte.delete()

    return redirect("finalizar_transporte")
