import unittest
from datetime import datetime


def has_friday_13(year: int, month: int) -> bool:
    """Esta funcion retorna verdadero si para un año y mes dado existe un viernes 13

    Args:
        year (int):
        month (int):

    Returns:
        bool:
    """
    if not isinstance(year, int):
        raise TypeError("Year invalid, enter a valid integer number")
    if not isinstance(month, int):
        raise TypeError("Month invalid, enter a valid integer number")

    return datetime(year, month, 13).weekday() == 4


class TestIsFriday13(unittest.TestCase):
    def setUp(self):
        self.is_friday_13 = {"year": 2023, "month": 10}
        self.not_friday_13 = {"year": 2023, "month": 7}

    def test_invalid_year(self):
        with self.assertRaises(TypeError):
            has_friday_13(year="1520", month=7)

    def test_invalid_month(self):
        with self.assertRaises(TypeError):
            has_friday_13(year=1520, month=(1520, 1))

    def test_expected_return(self):
        self.assertIsInstance(has_friday_13(year=1520, month=7), bool)

    def test_valid_friday_13(self):
        self.assertIs(
            has_friday_13(
                year=self.is_friday_13["year"], month=self.is_friday_13["month"]
            ),
            True,
        )

    def test_invalid_friday_13(self):
        self.assertIsNot(
            has_friday_13(
                year=self.not_friday_13["year"], month=self.not_friday_13["month"]
            ),
            True,
        )

if __name__ == "__main__":
    unittest.main()
