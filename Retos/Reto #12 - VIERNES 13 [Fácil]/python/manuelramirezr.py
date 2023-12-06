import calendar
import unittest

# Function to check if a date is friday thirteen
def is_friday_thirteen(month, year):
    return calendar.weekday(year, month, 13) == 4

# Unit test to is friday thirteen
class TestIsFridayThirteen(unittest.TestCase):
    def test_is_friday_thirteen(self):
        self.assertTrue(is_friday_thirteen(3, 2020))
        self.assertTrue(is_friday_thirteen(10, 2017))
        self.assertTrue(is_friday_thirteen(1, 1985))
        self.assertFalse(is_friday_thirteen(10, 2015))
        self.assertFalse(is_friday_thirteen(1, 1984))
        self.assertFalse(is_friday_thirteen(3, 2021))

if __name__ == '__main__':
    unittest.main()

