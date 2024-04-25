from click import option
from django.db import models


class Paciente(models.Model):

    class Status(models.IntegerChoices):
        ATIVO = 1, "Ativo"
        INATIVO = 2, "Inativo"

    nome = models.CharField(max_length=60)
    data_de_nascimento = models.DateTimeField()
    genero = models.IntegerField()
    cartao_sus = models.CharField(max_length=15, unique=True)
    telefone = models.CharField(max_length=15)
    rua = models.CharField(max_length=80)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=60)
    ponto_referencia = models.CharField(max_length=60)

    status = models.IntegerField(default=Status.ATIVO)

    data_criacao = models.DateTimeField(auto_created=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} {self.sobre_nome}"

    class Meta:
        db_table = "pacientes"
