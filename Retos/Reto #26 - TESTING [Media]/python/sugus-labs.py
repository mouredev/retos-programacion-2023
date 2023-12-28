from datetime import date
import unittest

def friday_13th_exists(year, month):
    
    dt = date(
        year = int(year), 
        month = int(month), 
        day = 13)
    is_friday = (dt.weekday == 4)
        
    return dt, is_friday

class Test(unittest.TestCase):
    
    def test_friday_13th_exists(self):
        self.assertEqual(friday_13th_exists("2023", "07"), \
            (date(year = 2023, month = 7, day = 13), False))
        self.assertEqual(friday_13th_exists("2023", "08"), \
            (date(year = 2023, month = 8, day = 13), False))
        self.assertEqual(friday_13th_exists("2023", "01"), \
            (date(year = 2023, month = 1, day = 13), True))  
        
    def test_friday_13th_inputs(self):
        year = "2021"
        month = "Sep"
        with self.assertRaises(TypeError):
            result = friday_13th_exists(year, month)

                                              
if __name__ == "__main__":

    year = "2023"
    month = "09"
    dt, is_friday = friday_13th_exists(year, month)
    print(f"{dt} is friday?: {is_friday}")
    
    print("-- Unit tests --")
    unittest.main()
    #print("Everything passed!")
