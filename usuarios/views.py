from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    print("chegando aqui login")
    return render(request, 'login.html')


def logout(request):
    return render(request, 'login.html')


def cadastro(request):

    return render(request, 'forms.html')


def lista_usuarios(request):

    return render(request, 'lista.html')


# @login_required(login_url='/auth/login')
# def master(request):
#     return render(request, 'templates/master.html')
