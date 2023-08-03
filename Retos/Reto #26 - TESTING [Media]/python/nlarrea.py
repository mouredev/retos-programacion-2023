"""
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
"""

import unittest
from datetime import datetime


def is_friday_thirteen(month, year):
    if not isinstance(month, int) or not isinstance(year, int):
        assert TypeError("Invalid month or year. Use integer numbers.")

    if month < 1 or month > 12:
        return "Month is out of range."
    
    date = datetime(year, month, 13)
    return date.weekday() == 4


class TestReto12(unittest.TestCase):
    def test_number_month(self):
        is_friday_13th = is_friday_thirteen(1, 2023)
        self.assertTrue(is_friday_13th)

        is_friday_13th = is_friday_thirteen(3, 2022)
        self.assertFalse(is_friday_13th)

    def test_month_out_of_range(self):
        is_friday_13th = is_friday_thirteen(14, 2023)
        self.assertEqual(is_friday_13th, "Month is out of range.")
        
        is_friday_13th = is_friday_thirteen(-1, 2023)
        self.assertEqual(is_friday_13th, "Month is out of range.")

    def test_not_numeric_values(self):
        with self.assertRaises(TypeError):
            is_friday_thirteen("6", 1998)

        with self.assertRaises(TypeError):
            is_friday_thirteen(6, "1998")


if __name__ == "__main__":
    unittest.main()