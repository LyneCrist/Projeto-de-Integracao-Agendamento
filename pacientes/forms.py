from django import forms


class PacienteForm(forms.Form):

    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.CharField(label="Email", max_length=100)
    telefone = forms.CharField(label="Telefone", max_length=100)
    dataNascimento = forms.CharField(label="Data Nascimento", max_length=100)
    estadoCivil = forms.CharField(label="Estado Civil", max_length=100)
    genero = forms.CharField(label="Genero", max_length=100)
    bairro = forms.CharField(label="Bairro", max_length=100)
    uf = forms.CharField(label="UF", max_length=100)
    municipio = forms.CharField(label="Município", max_length=100)
    nascionalidade = forms.CharField(label="Nascionalidade", max_length=100)
