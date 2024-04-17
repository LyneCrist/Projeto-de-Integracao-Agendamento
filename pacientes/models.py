from enum import IntEnum
from django.db import models


class Paciente(models.Model):

    class Status(models.IntegerChoices):
        ATIVO = 1
        INATIVO = 2

    nome = models.CharField(max_length=30)
    sobre_nome = models.CharField(max_length=60)
    data_de_nascimento = models.DateTimeField()
    genero = models.IntegerField()
    cartao_sus = models.CharField(max_length=15, unique=True)
    telefone = models.CharField(max_length=14)
    rua = models.CharField(max_length=60)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=60)
    ponto_referencia = models.CharField(max_length=50)

    status = models.IntegerField(default=Status.ATIVO)

    data_criacao = models.DateTimeField()
    data_alteracao = models.DateTimeField()

    def __str__(self):
        return f"{self.nome} {self.sobre_nome}"

    class Meta:
        db_table = "pacientes"
