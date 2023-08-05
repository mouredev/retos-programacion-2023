
'''
 Crea tres test sobre el reto 12: "Viernes 13".
 - Puedes copiar una solución ya creada por otro usuario en
   el lenguaje que estés utilizando.
 - Debes emplear un mecanismo de ejecución de test que posea
   el lenguaje de programación que hayas seleccionado.
 - Los tres test deben de funcionar y comprobar
   diferentes situaciones (a tu elección).
'''

import datetime
import unittest


# Solución de MoureDev al Reto #12: "Viernes 13"
def friday_13(year: int, month: int) -> bool:
    try:
        return datetime.date(year, month, 13).weekday() == 4
    except:
        return False
    
class TestViernes13(unittest.TestCase):
    
    def test_viernes13_found(self):
        resultado = friday_13(2023, 1)
        self.assertEqual(resultado, True)
    
    def test_viernes13_not_found(self):
        resultado = friday_13(2023, 3)
        self.assertEqual(resultado, False)
        
    def test_valores_incoherentes(self):
        resultado = friday_13(-2023, 15)
        self.assertEqual(resultado, False)
    
    def test_valores_no_int(self):
        resultado = friday_13("Brais", "Moure")
        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()