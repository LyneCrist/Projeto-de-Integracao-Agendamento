from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')

# @login_required(login_url='/auth/login')


def logout(request):
    return render(request, 'login.html')

# @login_required(login_url='/auth/login')


def listar(request):

    return render(request, 'lista.html')

# @login_required(login_url='/auth/login')


def cadastrar(request):

    return render(request, 'forms.html')

# @login_required(login_url='/auth/login')


def editar(request, id):

    return render(request, 'forms.html')

# @login_required(login_url='/auth/login')


def excluir(request, id):

    return render(request, 'lista.html')
