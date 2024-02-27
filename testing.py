import unittest
import re
from datetime import datetime
from helper import extraer_fecha

class TestExtraerFecha(unittest.TestCase):

    def test_fecha_valida(self):
        self.assertEqual(extraer_fecha("LISTA DE PRECIOS 01 DE ENERO DE 2020 NRO. 1"), datetime(2020, 1, 1))

    def test_string_invalido(self):
        self.assertIsNone(extraer_fecha("LISTA DE PRECIOS XX DE ENERO DE 2020 NRO. 1"))

    def test_fecha_inconsistente(self):
        self.assertIsNone(extraer_fecha("LISTA DE PRECIOS 31 DE FEBRERO DE 2020 NRO. 2"))

    def test_error_de_tipeo(self):
        self.assertIsNone(extraer_fecha("LISTA DE PRECIOS 01 DE ENRO DE 2020 NRO. 1"))

if __name__ == '__main__':
    unittest.main()
