from tkinter import Widget
from django import forms
from .utils import GENERO_CHOICES
from .models import Paciente
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    RegexValidator,
)


class PacienteForm(forms.ModelForm):

    nome = forms.CharField(
        validators=[
            MinLengthValidator(
                3, "Limite mínimo de 3 caracteres permitido para campo Nome"
            ),
            MaxLengthValidator(
                30,
                message="Limite máximo de 30 caracteres permitido para campo Nome",
            ),
            RegexValidator(
                regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
                message="Informe apenas texto para campo Nome",
            ),
        ],
        required=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "olá papai",
                "name": "nome",
                "id": "nome",
            }
        ),
    )

    # nome = (
    #     forms.CharField(
    #         validators=[
    #             MinLengthValidator(
    #                 3, "Limite mínimo de 3 caracteres permitido para campo Nome"
    #             ),
    #             MaxLengthValidator(
    #                 30,
    #                 message="Limite máximo de 30 caracteres permitido para campo Nome",
    #             ),
    #             RegexValidator(
    #                 regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
    #                 message="Informe apenas texto para campo Nome",
    #             ),
    #         ],
    #         max_length=30,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "placeholder": "* Nome",
    #                 "class": "form-text-input",
    #                 "name": "nome",
    #                 "id": "nome",
    #             }
    #         ),
    #     ),
    # )

    # sobre_nome = (
    #     forms.CharField(
    #         validators=[
    #             MinLengthValidator(3, "Limite mínimo de 3 caracteres"),
    #             MaxLengthValidator(
    #                 60,
    #                 message="Limite máximo de 30 caracteres",
    #             ),
    #             RegexValidator(
    #                 regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
    #                 message="Formato texto inválido",
    #             ),
    #         ],
    #         max_length=60,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "placeholder": "* Sobre nome",
    #                 "class": "form-text-input",
    #                 "name": "sobreNome",
    #                 "id": "sobreNome",
    #             }
    #         ),
    #     ),
    # )

    # # '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2024-01-15', '01/15/2024', '01/15/24'
    # data_de_nascimento = (
    #     forms.DateField(
    #         required=True,
    #         widget=forms.DateInput(
    #             format="%m/%d/%Y",
    #             attrs={
    #                 "type": "date",
    #                 "placeholder": "* dd/mm/yyyy",
    #                 "class": "form-text-input",
    #                 "name": "dataNascimento",
    #                 "id": "dataNascimento",
    #             },
    #         ),
    #         error_messages={"invalid": "Formato data inválido"},
    #     ),
    # )

    # genero = forms.ChoiceField(choices=GENERO_CHOICES, widget=forms.RadioSelect())

    # cartao_sus = forms.CharField()

    # telefone = (
    #     forms.CharField(
    #         validators=[
    #             RegexValidator(
    #                 regex=r"(\([0-9]{2}\))\s([9]{1})?([0-9]{4})-([0-9]{4})",
    #                 message="Formato inválido",
    #             ),
    #         ],
    #         max_length=15,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "type": "tel",
    #                 "placeholder": "* (99) 9999-9999",
    #                 "class": "form-text-input",
    #                 "name": "telefone",
    #                 "id": "telefone",
    #             }
    #         ),
    #     ),
    # )

    # rua = (
    #     forms.CharField(
    #         validators=[
    #             MinLengthValidator(5, "Limite mínimo de 5 caracteres"),
    #             MaxLengthValidator(
    #                 80,
    #                 message="Limite máximo de 80 caracteres",
    #             ),
    #             RegexValidator(
    #                 regex=r"^([a-zA-Zà-úÀ-Ú0-9]|-|_|.|º|\s)+$",
    #                 message="Formato texto inválido",
    #             ),
    #         ],
    #         max_length=60,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "placeholder": "* Sobre nome",
    #                 "class": "form-text-input",
    #                 "name": "sobreNome",
    #                 "id": "sobreNome",
    #             }
    #         ),
    #     ),
    # )

    # numero = (
    #     forms.IntegerField(
    #         required=True,
    #         widget=forms.NumberInput(
    #             attrs={
    #                 "placeholder": "* Número",
    #                 "class": "form-text-input",
    #                 "name": "sobreNome",
    #                 "id": "sobreNome",
    #             }
    #         ),
    #         error_messages={"invalid": "Campo necessário"},
    #     ),
    # )

    # complemento = (
    #     forms.CharField(
    #         validators=[
    #             MinLengthValidator(5, "Limite mínimo de 5 caracteres"),
    #             MaxLengthValidator(
    #                 60,
    #                 message="Limite máximo de 60 caracteres",
    #             ),
    #             RegexValidator(
    #                 regex=r"[^A-Za-z0-9\\s]+",
    #                 message="Formato texto inválido",
    #             ),
    #         ],
    #         max_length=60,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "placeholder": "Sobre nome",
    #                 "class": "form-text-input",
    #                 "name": "sobreNome",
    #                 "id": "sobreNome",
    #             }
    #         ),
    #     ),
    # )

    # ponto_referencia = (
    #     forms.CharField(
    #         validators=[
    #             RegexValidator(
    #                 regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
    #                 message="Formato texto inválido",
    #             ),
    #         ],
    #         max_length=15,
    #         required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 "placeholder": "",
    #                 "class": "form-text-input",
    #                 "name": "pontoReferencia",
    #                 "id": "pontoReferencia",
    #             }
    #         ),
    #     ),
    # )

    # def clean(self):

    #     super(PacienteForm, self).clean()

    # nome = forms.CharField(
    #     validators=[
    #         # MinLengthValidator(
    #         #     3, "Limite mínimo de 3 caracteres permitido para campo Nome"
    #         # ),
    #         MaxLengthValidator(
    #             30,
    #             message="Limite máximo de 30 caracteres permitido para campo Nome",
    #         ),
    #         RegexValidator(
    #             regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
    #             message="Informe apenas texto para campo Nome",
    #         ),
    #     ],
    #     error_messages={"required": "Campo necessário"},
    # )

    class Meta:

        model = Paciente

        # fields = "__all__"
        fields = ["nome"]

        exclude = ["status", "data_criacao", "data_alteracao"]

        # fields = {
        #     "nome": forms.CharField(
        #         validators=[
        #             MinLengthValidator(
        #                 3, "Limite mínimo de 3 caracteres permitido para campo Nome"
        #             ),
        #             MaxLengthValidator(
        #                 30,
        #                 message="Limite máximo de 30 caracteres permitido para campo Nome",
        #             ),
        #             RegexValidator(
        #                 regex=r"^([a-zA-Zà-úÀ-Ú]\s)+$",
        #                 message="Informe apenas texto para campo Nome",
        #             ),
        #         ],
        #         max_length=100,
        #         help_text="100 characters max.",
        #     )
        # }

        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "id": "nome",
                    "name": "nome",
                    "placeholder": "* Nome",
                }
            ),
        }

    def clean_nome(self):

        nome = self.cleaned_data.get("nome")

        if not nome:
            raise forms.ValidationError("Campo necessário")

        return nome

    def clean(self):

        cleaned_data = super().clean()

        nome = cleaned_data.get("nome")

        sobre_nome = cleaned_data.get("sobreNome")

        if not nome:
            raise forms.ValidationError("Campo necessário")

        if not sobre_nome:
            raise forms.ValidationError("Campo necessário")
