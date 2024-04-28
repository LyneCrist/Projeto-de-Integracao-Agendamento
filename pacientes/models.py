from click import option
from django.db import models
from .utils import AGENDAMENTO_FIXO_CHOICES, GENERO_CHOICES


class Paciente(models.Model):

    class Status(models.IntegerChoices):
        ATIVO = 1, "Ativo"
        INATIVO = 2, "Inativo"

    nome = models.CharField(max_length=60, null=False, blank=False)

    data_de_nascimento = models.DateField(null=True)

    genero = models.IntegerField(choices=GENERO_CHOICES, null=True)

    # cartao_sus = models.CharField(
    #     max_length=15, unique=True, blank=False, null=False, default=None
    # )

    cartao_sus = models.CharField(max_length=15, unique=True, null=True)

    agendamento_fixo = models.IntegerField(
        choices=AGENDAMENTO_FIXO_CHOICES,
        default=Status.ATIVO,
    )

    telefone = models.CharField(max_length=18)
    rua = models.CharField(max_length=50)
    numero = models.IntegerField(null=True)
    complemento = models.CharField(max_length=40)
    ponto_referencia = models.CharField(max_length=40)

    status = models.IntegerField(default=Status.ATIVO)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        db_table = "pacientes"
