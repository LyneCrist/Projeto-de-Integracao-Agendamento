from django.shortcuts import render, redirect
from .forms import TransporteForm
from .models import Transporte

from django.contrib import messages


def listar(request):

    context = {}

    context["transportes"] = Transporte.objects.all()[:15]

    return render(request, "lista_transportes.html", context)


def cadastrar(request):

    context = {}

    context["title"] = "Cadastra Transporte"

    if request.method == "POST":

        context["form"] = TransporteForm(request.POST)

        if context["form"].is_valid():
            try:

                # print(context["form"].cleaned_data)

                context["form"].save()

                messages.success(request, "Transporte cadastrado com sucesso")

                return redirect("listar_transportes")

            except:

                messages.error(
                    request, "Ocorreu um erro durante o registo, tente novamente"
                )

                return render(request, "criar_transporte.html", context)

        context["erros"] = context["form"].errors.as_data()

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
