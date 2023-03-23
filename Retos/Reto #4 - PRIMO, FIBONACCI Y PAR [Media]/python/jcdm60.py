# Reto #4: PRIMO, FIBONACCI Y PAR
#### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23

## Enunciado

#
# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#

import math


class Number_PFP:
    def __init__(self, number):
        self.number = number

    def isPerfectSquare(self, x):
        s = int(math.sqrt(x))
        return s * s == x

    def isFibonacci(self):
        return self.isPerfectSquare(
            5 * self.number * self.number + 4
        ) or self.isPerfectSquare(5 * self.number * self.number - 4)

    def isPrime(self):
        if self.number == 2 or self.number == 3:
            return True
        if self.number % 2 == 0 or self.number < 2:
            return False
        for n in range(3, int(self.number**0.5) + 1, 2):
            if self.number % n == 0:
                return False
        return True

    def isOdd(self):
        flag = False
        if self.number % 2:
            flag = True
        return flag


if __name__ == "__main__":
    number = int(input("Digite un número entero positivo: "))
    finonacci = Number_PFP(number)
    result_pri = finonacci.isPrime()
    result_fib = finonacci.isFibonacci()
    result_odd = finonacci.isOdd()

    text_pri = "es primo," if result_pri else "no es primo,"
    text_fib = "fibonacci" if result_fib else "no es fibonacci"
    text_odd = "y es impar" if result_odd else "y es par"

    print(f"{number} {text_pri} {text_fib} {text_odd}")
