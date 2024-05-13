import unittest

def fizz_buzz():
    """funcion que genera una secuancia de numeros del 1 al 100, reemplazando
    los numeros que son multiplos de 3 por "fizz", y los que son multiplos de 5
    por "buzz", si el numero es multiplo de ambos "fizzbuzz", en caso de que no sea
    multiplo de ninguno deja el numero
    Returns:
        list: una lista que contiene la secuancia de numeros del 1 al 100 remplazados
        por sus respectivas palabras segun la condicion
    """
    result = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(i)
    return result

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizz_buzz()[2], "fizz") 
        self.assertEqual(fizz_buzz()[5], "fizz")
        self.assertEqual(fizz_buzz()[8], "fizz")

    def test_buzz(self):
        self.assertEqual(fizz_buzz()[4], "buzz")
        self.assertEqual(fizz_buzz()[19], "buzz")
        self.assertEqual(fizz_buzz()[24], "buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizz_buzz()[14], "fizzbuzz")
        self.assertEqual(fizz_buzz()[29], "fizzbuzz")
        self.assertEqual(fizz_buzz()[44], "fizzbuzz")
        
    def test_normal(self):
        self.assertEqual(fizz_buzz()[0], 1)
        self.assertEqual(fizz_buzz()[1], 2)
        self.assertEqual(fizz_buzz()[97], 98)
        


if __name__ == "__main__":
    unittest.main()