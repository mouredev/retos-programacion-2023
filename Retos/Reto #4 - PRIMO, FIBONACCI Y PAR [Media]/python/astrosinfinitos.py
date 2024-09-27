#
# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#

num = int(input("Introduce un número: "))

# Función para comprobar que el número introducido es primo


def es_primo(num):
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "no es un número primo")
            return False
        print(num, "es un número primo")
        return True


# Función para comprobar que el número es par o impar


def es_par(num):
    if num % 2 == 0:
        print(num, "es par")
        return True
    else:
        print(num, "es impar")
        return False


# Función para realizar la sucesión de Fibonacci con el número dado


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
