# de Akihiro93
from datetime import datetime
import unittest

def viernes_trece (año, mes, dia):
    fecha = datetime(año, mes, dia)
    dia_es = fecha.strftime("%A")
    if dia_es == "Friday":
        return True # Cambiado para la verificación
    else:
        return False # Cambiado para la verificación

class Test (unittest.TestCase):

    def test_April (self):
        result = viernes_trece(2023, 1, 13)
        self.assertTrue(result, "debería ser true" )

    def test_February (self):
        result = viernes_trece(2045, 2, 13)
        self.assertFalse(result, "debería ser False" )

    def test_January (self):
        result = viernes_trece(2023, 3, 13) # 2023, 10, 13 para causar un fallo
        self.assertFalse(result, "debería ser False" )

if __name__ == "main":
    unittest.main()
