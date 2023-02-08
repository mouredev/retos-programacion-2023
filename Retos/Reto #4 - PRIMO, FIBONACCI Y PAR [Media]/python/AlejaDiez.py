# Si es divisible entre dos es par
def esPar(num) -> bool:
    return num % 2 == 0

def esPrimo(num) -> bool:
    if num < 2: # Los números menores a 2 no son primos
        return False
    elif num != 2 and esPar(num): # Los números pares excepto el 2 no son primos
        return False
    else:
        for x in range(3, num): # Si es divisible por algún número anterior no es primo
            if num % x == 0:
                return False
        return True

def esFibonacci(num) -> bool:
    fibonacci = [0, 1]

    # Suma de los dós últimos números
    def sumaUltimosElementos() -> int:
        return fibonacci[-2] + fibonacci[-1]

    while fibonacci.count(num) == 0: # Comprobación de que el número esta en la lista
        if sumaUltimosElementos() > num:
            return False
        else:
            fibonacci.append(sumaUltimosElementos())
    return True

try:
    numero = int(input("Introduce un número: "))

    print(f"  - Es par: {esPar(numero)}")
    print(f"  - Es primo: {esPrimo(numero)}")
    print(f"  - Es Fibonacci: {esFibonacci(numero)}")
except ValueError:
    print("Tienes que introducir un número entero.")
