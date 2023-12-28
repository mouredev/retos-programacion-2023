from datetime import datetime
import unittest

def FridayThe13th(month, year):
    date = datetime(year, month, 13)

    return True if date.weekday() == 4 else False

class test_viernes_13(unittest.TestCase):
    def test_1(self):
        self.assertTrue(FridayThe13th(1,2023))
    def test_2(self):
        self.assertEqual(FridayThe13th(1,2025),False)
    def test_3(self):
        with self.assertRaises(TypeError):
            FridayThe13th("01","2026")
    def test_4(self):
        self.assertEqual(FridayThe13th("1","2023"),True)


if __name__ == '__main__':
    unittest.main()


