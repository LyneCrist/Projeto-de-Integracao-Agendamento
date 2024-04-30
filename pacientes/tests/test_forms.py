from unicodedata import numeric
from django.test import TestCase
from ..forms import PacienteForm
import re


class PacienteFormTestCase(TestCase):

    def setUp(self):

        self.alpha_pattern = "[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\\-_\\s]+$"

        self.alpha_numeric_pattern = "[A-Za-z0-9_À-ÿ.-_\\s]+$"

        self.numeric_pattern = "[^0-9]"

        self.phone_number_pattern = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

        self.phone_number = "+55(62) +._=98833-91509"

    def test_acerto_para_formato_numerico_campo_telefone(self):

        self.assertTrue(
            re.sub(self.numeric_pattern, "", self.phone_number).isnumeric(),
            "Formato inválido para telefone",
        )

    def test_falha_no_formato_campo_nome(self):

        nome = "Tatiane Eliane. Aparício"

        self.assertIsNone(re.match(self.alpha_pattern, nome))
