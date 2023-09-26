from math import sqrt

numero_1 = int(input("Introduce un numero: "))

def primos(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(2, int(sqrt(n))):
            if n % i == 0:
                return False
            else:
                return False
        return True
    
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

fibonacci = [0,1,2,3,5,8,13,21,34,55,89]

if primos(numero_1) == True:
    print(f"El numero {numero_1} es primo")
else:
    print(f"El numero {numero_1} no es primo")

if par(numero_1) == True:
    print(f"El numero {numero_1} es par")
else:
    print(f"El numero {numero_1} es impar")

if fibonacci.count(numero_1) == 1:
    print(f"El numero {numero_1} es un numero de la serie de Fibonacci")
else:
    print(f"El numero {numero_1} no es un numero de la serie de Fibonacci")