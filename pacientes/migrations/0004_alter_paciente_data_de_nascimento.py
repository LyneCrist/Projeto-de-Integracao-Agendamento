# Generated by Django 5.0.4 on 2024-04-26 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "pacientes",
            "0003_remove_paciente_sobre_nome_paciente_agendamento_fixo_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="paciente",
            name="data_de_nascimento",
            field=models.DateField(),
        ),
    ]
