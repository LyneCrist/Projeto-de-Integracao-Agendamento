from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.login, name="logout"),
    path('cadastro/', views.cadastro, name="cadastro_usuario"),
    path('lista/', views.lista_usuarios, name="lista_usuarios"),
]
