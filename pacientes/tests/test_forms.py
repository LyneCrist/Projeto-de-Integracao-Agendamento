from django.test import TestCase
from ..forms import PacienteForm
import re


class PacienteModelTests(TestCase):

    validAlpha = "[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\\-_\\s]+$"

    validAlphaNumeric = "[A-Za-z0-9_À-ÿ.-_\\s]+$"

    def test_falha_no_formato_campo_nome(self):

        nome = "Tatiane Eliane. Aparício"

        self.assertIs(re.match(self.validAlpha, nome), None)
