""" 
## Enunciado
<<<<<<< HEAD
=======

```
>>>>>>> cfbdbf06a332a75f42bb1db9cef090643e93d2ca
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
```

"""

def fizz_buzz():
# The code is implementing the FizzBuzz problem. It iterates through the numbers from 1 to 100
# (inclusive) using a for loop. For each number, it checks if it is divisible by 15 (both 3 and 5), in
# which case it prints "fizzbuzz". If the number is only divisible by 5, it prints "buzz". If the
# number is only divisible by 3, it prints "fizz". If the number is not divisible by either 3 or 5, it
# simply prints the number itself.
    for number in range(1,101):
        if number % 15 == 0:
            print('fizzbuzz')
        elif number % 5 == 0:
            print('buzz')
        elif number % 3 == 0:
            print('fizz')
        else:
            print(number)
        
fizz_buzz()