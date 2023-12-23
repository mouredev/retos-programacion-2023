"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
      return "fizzbuzz"
    elif number % 3 == 0:
      return "fizz"
    elif number % 5 == 0:
      return "buzz"
    else:
      return str(number)  

for number in range(1, 101):
    result = fizzbuzz(number)
    print(result)

