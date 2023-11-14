import unittest
import datetime

def es_viernes_13(mes, año):
    fecha = datetime.datetime(año, mes, 13)
    return fecha.weekday() == 4

class TestViernes13(unittest.TestCase):

    def test_viernes_13_valido(self):
        # Prueba para un viernes 13 válido
        self.assertTrue(es_viernes_13(3, 2023))  # Marzo de 2023 es un viernes 13 válido

    def test_viernes_13_no_valido(self):
        # Prueba para un viernes 13 no válido
        self.assertFalse(es_viernes_13(5, 2022))  # Mayo de 2022 no es un viernes 13 válido

    def test_viernes_13_limite(self):
        # Prueba para el límite de los años
        self.assertTrue(es_viernes_13(1, 2100))  # Enero de 2100 es un viernes 13 válido

if __name__ == '__main__':
    unittest.main()
