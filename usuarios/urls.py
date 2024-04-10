from django.urls import path
from . import views

url_patterns = [
    path('', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro_usuario"),
]
