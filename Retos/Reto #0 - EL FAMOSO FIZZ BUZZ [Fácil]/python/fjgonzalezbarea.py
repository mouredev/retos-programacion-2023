"""
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

 Ejecución:
 python -m fjgonzalezbarea
"""

def is_divisible_by(number, divisor):
    return number % divisor == 0

def print_fizz_buzz():
    for index in range(1, 100):
        if is_divisible_by(index, 3) and is_divisible_by(index, 5):
            print("fizzbuzz")
        elif is_divisible_by(index, 3):
            print("fizz")
        elif is_divisible_by(index, 5):
            print("buzz")
        else:
            print(index)

if __name__ == "__main__":
    print_fizz_buzz()
