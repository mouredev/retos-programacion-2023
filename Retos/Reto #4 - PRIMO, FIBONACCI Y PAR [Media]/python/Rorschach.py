# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
#  la que el siguiente siempre es la suma de los dos anteriores.
#  0, 1, 1, 2, 3, 5, 8, 13...

num = int(input("Introduce un número: "))  # Convertir la entrada a un entero


def es_primo(num):
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "no es un numero primo")
            return False
    print(num, "es un numero primo")
    return True


def es_par(num):
    if num % 2 == 0:
        print(num, "es par")
        return True
    else:
        print(num, "es impar")
        return False


def fibonacci(num):
    anterior = 0
    actual = 1
    for k in range(num):
        siguiente = anterior + actual
        anterior = actual
        actual = siguiente
    return actual


resultado = fibonacci(num)
primo = es_primo(num)
par = es_par(num)
print(
    f"El número de Fibonacci correspondiente es: {resultado}"
)  # Uso de f-string para formatear la salida
