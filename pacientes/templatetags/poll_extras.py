from django import template
from django.forms.boundfield import BoundField

register = template.Library()


@register.filter(name="set_column_label")
def set_column_label(field: BoundField) -> str:

    fields = {
        "nome": "col-1",
        "data_de_nascimento": "col-2",
        "cartao_sus": "col-1",
        "telefone": "col-1",
        "rua": "col-1",
        "numero": "col-1",
        "complemento": "col-1",
        "ponto_referencia": "col-2",
    }

    # print(f"{type(field)} {fields[field.name]} {field.name}")

    return fields[field.name]


@register.filter(name="set_column_input")
def set_column_input(field: BoundField) -> str:

    fields = {
        "nome": "col-5",
        "data_de_nascimento": "col-1",
        "genero": "col-5",
        "cartao_sus": "col-2",
        "agendamento_fixo": "col-5",
        "telefone": "col-2",
        "rua": "col-5",
        "numero": "col-1",
        "complemento": "col-4",
        "ponto_referencia": "col-4",
    }

    return fields[field.name]
