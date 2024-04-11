from django.shortcuts import render


def lista_pacientes(request):

    return render(request, "lista_pacientes.html")


def cadastro(request):

    return render(request, "forms.html")
