import unittest

leet_dict = {
    'a': '4',
    'b': '8',
    'c': '<',
    'd': '|)',
    'e': '3',
    'f': '|=',
    'g': '9',
    'h': '|-|',
    'i': '1',
    'j': '_|',
    'k': '|<',
    'l': '|_',
    'm': '|\\|',
    'n': '|\\|',
    'o': '0',
    'p': '|o',
    'q': '()_',
    'r': '|2',
    's': '$',
    't': '7',
    'u': '|_|',
    'v': '\\/',
    'w': '\\/\\/',
    'x': '><',
    'y': '`/',
    'z': '2',
    '1': '!',
    '2': '@',
    '3': '#',
    '4': '$',
    '5': '%',
    '6': '^',
    '7': '&',
    '8': '*',
    '9': '(',
    '0': '°'
}
def leet_lenguage(string: str) -> str : 
    """función que convierte un string en lenguaje leet (1337)

    Args:
        string (str): palabra o frase que se quiere convertir
    Returns:
        str: el string convertido a lenguaje leet
    """
    leet = ""
    for i in string.lower():
        if i in leet_dict:
            leet += leet_dict[i]
        else:
            leet += i
    return leet

class TestLeet(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(leet_lenguage("hola"), "|-|0|_4")
    def test_case(self):
        self.assertEqual(leet_lenguage("COmo"), "<0|\\|0")
    def test_frase(self):
        self.assertEqual(leet_lenguage("Perry el Ornitorrinco"), "|o3|2|2`/ 3|_ 0|2|\\|170|2|21|\\|<0")
    def test_numbers_symbols(self):
        self.assertEqual(leet_lenguage("password123?"), "|o4$$\\/\\/0|2|)!@#?")


if __name__ == "__main__":
    unittest.main()