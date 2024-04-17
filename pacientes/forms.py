from typing import Any
from django import forms
from .models import Paciente
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class PacienteForm(forms.ModelForm):

    class Genero(models.IntegerChoices):
        FEMININO = 1
        MASCULINO = 2
        OUTROS = 3

    nome = (
        forms.CharField(
            validators=[
                MinValueValidator(
                    3, "Limite mínimo de 3 caracteres permitido para campo Nome"
                ),
                MaxValueValidator(
                    30,
                    message="Limite máximo de 30 caracteres permitido para campo Nome",
                ),
                RegexValidator(
                    regex=r"[^a-zA-Z_-\\s]+",
                    message="Informe apenas texto para campo Nome",
                ),
            ],
            required=True,
            max_length=30,
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Nome",
                    "class": "form-text-input",
                    "name": "name",
                    "id": "nome",
                }
            ),
        ),
    )

    sobre_nome = (
        forms.CharField(
            validators=[
                MinValueValidator(
                    3, "Limite mínimo de 3 caracteres permitido para 'Sobre nome'"
                ),
                MaxValueValidator(
                    60,
                    message="Limite máximo de 30 caracteres permitido para campo 'Sobre nome'",
                ),
                RegexValidator(
                    regex=r"[^a-zA-Z_-\\s]+",
                    message="Informe apenas texto para campo Sobre 'Sobre nome'",
                ),
            ],
            required=True,
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Sobre nome",
                    "class": "form-text-input",
                    "name": "sobreNome",
                    "id": "sobreNome",
                }
            ),
        ),
    )

    genero = forms.ChoiceField(choices=Genero, widget=forms.RadioSelect())

    def clean(self):

        super(PacienteForm, self).clean()

    class Meta:
        model = Paciente
        fields = (
            "nome",
            "email",
            "telefone",
            "dataNascimento",
            "genero",
            "bairro",
            "numero",
            "complemento",
            "ponto_de_refencia",
        )

    # nome = forms.CharField(label="Nome", max_length=100)
    # email = forms.CharField(label="Email", max_length=100)
    # telefone = forms.CharField(label="Telefone", max_length=100)
    # dataNascimento = forms.CharField(label="Data Nascimento", max_length=100)
    # genero = forms.CharField(label="Genero", max_length=100)
    # bairro = forms.CharField(label="Bairro", max_length=100)
    # numero = forms.CharField(label="Número", max_length=100)
    # complemento = forms.CharField(label="Complemento", max_length=100)
    # ponto_de_refencia = forms.CharField(label="Ponto de refencia", max_length=100)
