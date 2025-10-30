"""
Crea tres test sobre el reto 12: "Viernes 13".
- Puedes copiar una solución ya creada por otro usuario en
    el lenguaje que estés utilizando.
- Debes emplear un mecanismo de ejecución de test que posea
    el lenguaje de programación que hayas seleccionado.
- Los tres test deben de funcionar y comprobar
    diferentes situaciones (a tu elección).
"""

from datetime import date
import unittest

def have_friday_13(year: int, month: int) -> bool:
    """Check if the 13th of a given month/year falls on a Friday.

    Args:
        year (int): Year to check.
        month (int): Month to check (1-12).

    Returns:
        bool: True if the 13th is Friday, False otherwise.

    Raises:
        TypeError: If arguments are not integers.
        ValueError: If month is not in 1-12.
    """
    if not isinstance(year, int) or not isinstance(month, int):
        raise TypeError("El año y el mes deben ser enteros.")
    if not 1 <= month <= 12:
        raise ValueError("El mes debe estar entre 1 y 12.")

    return date(year, month, 13).weekday() == 4

class TestHaveFriday13(unittest.TestCase):
    """Unit test suite for the have_friday_13 function.

    Tests include:
    - Cases where Friday the 13th exists
    - Cases where it does not
    - Type validation errors
    - Month range validation
    """

    def test_1(self):
        """Check a month in 2023 that does have a Friday 13th."""
        result = have_friday_13(2023, 1)
        self.assertTrue(result)

    def test_2(self):
        """Check a month in 2023 that does not have a Friday 13th."""
        result = have_friday_13(2023, 3)
        self.assertFalse(result)

    def test_3(self):
        """Ensure TypeError is raised when passing non-integer values."""
        with self.assertRaises(TypeError):
            have_friday_13("s", "s")

    def test_4(self):
        """Ensure ValueError is raised when passing an out-of-range month."""
        with self.assertRaises(ValueError):
            have_friday_13(2024, 14)


if __name__ == "__main__":
    unittest.main()
