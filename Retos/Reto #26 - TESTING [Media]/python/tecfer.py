import unittest
from datetime import date

def friday_13(month, year) -> bool :
    try:
        return date(year, month, 13).isoweekday() == 5
    except:
        return False

class FridayTestCase(unittest.TestCase):

    def test_is_friday_13(self):
        day = friday_13(1,2023)
        self.assertTrue(day)

    def test_is_not_friday_13(self):
        day = friday_13(2,2023)
        self.assertFalse(day)
    
    def test_invalid_date(self):
        day = friday_13(13,2023)
        self.assertFalse(day)



if __name__ == '__main__':
    unittest.main()