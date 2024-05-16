import unittest
from unittest.mock import patch
import random
import string

def password_generator(length: int, upper: bool, numbers: bool, symbols: bool) -> str:
    password = string.ascii_lowercase
    if upper:
        password += string.ascii_uppercase
    if numbers:
        password += string.digits
    if symbols:
        password += string.punctuation
    
    return "".join(random.choice(password) for _ in range(length))  
    
def get_password_inputs():
    while True:
        try:
            length = int(input("Ingrese la longitud de la contraseña [8...16]: "))
            if length not in range(8, 17):
                print("La contraseña debe estar entre 8 y 16.")
                continue
            break
        except ValueError:
            print("ingrese un número valido.")
    while True:
        upper = input("¿Dese incluir caracteres en mayúscula? (s/n): "). lower()
        if upper in ["s", "n"]:
            upper = upper == "s"
            break
        else:
            print("Responda 's' para Si o 'n' para No.")
    while True:
        numbers = input("¿Desea incluir numeros? (s/n): ").lower()
        if numbers in ["s", "n"]:
            numbers = numbers == "s"
            break
        else:
            print("Responda 's' para Si o 'n' para No.")
    while True:
        symbols = input("Desea incluir simbolos? (s/n): ").lower()
        if symbols in ["s", "n"]:
            symbols = symbols == "s"
            break
        else:
            print("Responda 's' para Si o 'n' para No.")
    
    return length, upper, numbers, symbols



class TestPasgordGenerator(unittest.TestCase):
    @patch("builtins.input", side_effect=["10", "s", "s", "s"])
    def test_valid_inputs(self, mock_input):
        length, upper, numbers, symbols = get_password_inputs()
        self.assertEqual(length, 10)
        self.assertTrue(upper)
        self.assertTrue(numbers)
        self.assertTrue(symbols)
    
    @patch("builtins.input", side_effect=["10", "n", "n", "s"])
    def test_only_symbols(self, mock_input):
        length, upper, numbers, symbols = get_password_inputs()
        self.assertEqual(length, 10)
        self.assertFalse(upper)
        self.assertFalse(numbers)
        self.assertTrue(symbols)
    
    @patch("builtins.input", side_effect=["16", "s", "s", "n"])
    def test_only_upper_numbers(self, mock_input):
        length, upper, numbers, symbols = get_password_inputs()
        self.assertEqual(length, 16)
        self.assertTrue(upper)
        self.assertTrue(numbers)
        self.assertFalse(symbols)
        
if __name__ == "__main__":
    unittest.main()