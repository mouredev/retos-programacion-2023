"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizz_buzz() -> None:
    """
    Prints the numbers from 1 to 100 (inclusive), each on a new line.

    - Replaces multiples of 3 with the word "fizz".
    - Replaces multiples of 5 with the word "buzz".
    - Replaces multiples of both 3 and 5 with the word "fizzbuzz".
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0: 
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0: 
            print("buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizz_buzz()
