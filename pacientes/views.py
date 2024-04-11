from django.shortcuts import render


def lista_pacientes(request):

    return render(request, "lista_pacientes.html")


def cadastro(request):

    print("chegando aqui cadastro")

    return render(request, "cadastro_paciente.html", {})
