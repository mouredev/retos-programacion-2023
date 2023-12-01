#Toma del valor
n_1 = int(input("¿Cual es el numero?: "))

#Inportado la funcion sqrt
from math import sqrt

#Funcion para verificar si es primo
def primos (n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(2, int(sqrt(n))):
            if n % i == 0:
                return False
    return True

# Funcion para verificar si es par
def Par (n):
    if n % 2 == 0:
        return True
    else:
        return False

# Lista de Fibonacci
lista_de_Fibonacci = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Verificar si es primo
if primos(n_1) == True:
    print("El numero: ", n_1, " es primo")
else:
    print("El numero: ", n_1, " no es primo")

# Verificar si es par
if Par(n_1) == True:
    print("El numero: ", n_1, " es par")
else:
    print("El numero: ", n_1, " no es par")

# Verificar si es un numero de fibonacci
if lista_de_Fibonacci.count(n_1) == 1:
    print("El numero: ", n_1, " es fibonacci")
else:
    print("El numero: ", n_1, " no es fibonacci")
