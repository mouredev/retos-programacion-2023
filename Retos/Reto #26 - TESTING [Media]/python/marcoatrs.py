import unittest
from datetime import datetime


def check_friday(month: int, year: int) -> bool:
    day = datetime(year=year, month=month, day=13)
    return day.weekday() == 4


class TestCheckFriday(unittest.TestCase):
    def test_value_error(self):
        self.assertRaises(ValueError, check_friday, -5, 7)

    def test_true_answer(self):
        self.assertEqual(check_friday(1, 2023), True)

    def test_false_answer(self):
        self.assertEqual(check_friday(2, 2023), False)


unittest.main()
