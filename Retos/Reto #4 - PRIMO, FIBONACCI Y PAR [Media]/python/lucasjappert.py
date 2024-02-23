import unittest

def is_par(number: int):
    return number % 2 == 0

def is_prime(number: int):
    if number < 2: return False
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True

def is_fibonacci(number: int):
    prev_counter, current_counter = 0, 1
    while current_counter < number:
        current_counter += prev_counter
        prev_counter = current_counter - prev_counter
    return number in [prev_counter, current_counter]

# TESTS
class TestsReto4(unittest.TestCase):
    def test_is_par(self):
        self.assertEqual(is_par(0), True)
        self.assertEqual(is_par(1), False)
        self.assertEqual(is_par(2), True)
        self.assertEqual(is_par(3), False)

    def test_is_prime(self):
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(13), True)

    def test_is_fibonacci(self):
        self.assertEqual(is_fibonacci(0), True)
        self.assertEqual(is_fibonacci(1), True)
        self.assertEqual(is_fibonacci(2), True)
        self.assertEqual(is_fibonacci(3), True)
        self.assertEqual(is_fibonacci(4), False)
        self.assertEqual(is_fibonacci(5), True)
        self.assertEqual(is_fibonacci(6), False)
        self.assertEqual(is_fibonacci(7), False)
        self.assertEqual(is_fibonacci(8), True)
        self.assertEqual(is_fibonacci(9), False)


if __name__ == "__main__":
    unittest.main(exit=False)

    while True:
        user_input = input("--> Ingrese un número ('exit' para cerrar el programa): ")
        if user_input == "exit": break
        
        number = int(user_input)
        text1 = "es PAR" if is_par(number) else "es IMPAR"
        text2 = "es PRIMO" if is_prime(number) else "NO es PRIMO"
        text3 = "pertenece a la serie de Fibonacci" if is_fibonacci(number) else "NO pertenece a la serie de Fibonacci"
        print(f"El número ingresado es {number}. Este número {text1}, {text2} y {text3}.")

