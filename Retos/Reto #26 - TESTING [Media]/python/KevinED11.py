import unittest
from datetime import date


def is_friday_13(year: int, month: int) -> bool:
    if not isinstance(year, int) or not isinstance(month, int):
        raise TypeError("Invalid type, enter a valid integer number")

    return date(year=year,
                month=month,
                day=13).weekday() == 4


class TestIsFriday13(unittest.TestCase):
    def setUp(self):
        self.valid_friday_13 = is_friday_13(year=2023, month=1)
        self.invalid_friday_13 = is_friday_13(year=2023, month=2)

    def test_valid_expected_return_type(self):
        self.assertIsInstance(self.valid_friday_13, bool)

    def test_valid_friday_13(self):
        self.assertIs(self.valid_friday_13, True)

    def test_invalid_friday_13(self):
        self.assertIsNot(self.invalid_friday_13, True)

    def test_expected_error(self):
        with self.assertRaises(TypeError):
            is_friday_13(year=2023, month="2")


if __name__ == "__main__":
    unittest.main()
