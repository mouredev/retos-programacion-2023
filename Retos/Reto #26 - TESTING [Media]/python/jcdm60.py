# Reto #26: Testing
#### Dificultad: Media | Publicación: 26/06/23 | Corrección: 03/07/23

## Enunciado

#
# Crea tres test sobre el reto 12: "Viernes 13".
# - Puedes copiar una solución ya creada por otro usuario en
#   el lenguaje que estés utilizando.
# - Debes emplear un mecanismo de ejecución de test que posea
#   el lenguaje de programación que hayas seleccionado.
# - Los tres test deben de funcionar y comprobar
#   diferentes situaciones (a tu elección).
#

import unittest
import datetime


def is_friday_13(month, year):
    # Creamos un objeto datetime para el 13 del month y año indicados
    date = datetime.date(year, month, 13)

    # Comprobamos si es viernes (el número 4 representa el día viernes)
    if date.weekday() == 4:
        return True
    else:
        return False


class Friday13TestCase(unittest.TestCase):
    def test_friday_13(self):
        self.assertTrue(is_friday_13(1, 2023))  # Enero 2023, viernes 13
        self.assertFalse(is_friday_13(2, 2023))  # Febrero 2023, no es viernes 13


    def test_month_range(self):
        self.assertRaises(ValueError, is_friday_13, 0, 2023)  # Mes < 1
        self.assertRaises(ValueError, is_friday_13, 13, 2023)  # Mes > 12

    def test_year_type(self):
        self.assertRaises(TypeError, is_friday_13, 1, "2023")  # Año no es un número entero        
        
if __name__ == "__main__":
    unittest.main()
