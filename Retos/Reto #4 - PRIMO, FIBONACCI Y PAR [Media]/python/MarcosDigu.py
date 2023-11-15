def es_primo(num):
    """Verifica si un número es primo."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def es_numero_fibonacci(num):
    """Verifica si un número es un número de Fibonacci."""
    def es_cuadrado_perfecto(n):
        """Verifica si un número es un cuadrado perfecto."""
        raiz = int(n**0.5)
        return n == raiz**2

    return es_cuadrado_perfecto(5 * num**2 + 4) or es_cuadrado_perfecto(5 * num**2 - 4)

def es_par(num):
    """Verifica si un número es par."""
    return num % 2 == 0

def checker(num):
    """Imprime información sobre si un número es primo, de Fibonacci y par."""
    primo = "primo" if es_primo(num) else "compuesto"
    fibo = "fibonacci" if es_numero_fibonacci(num) else "no fibonacci"
    par = "par" if es_par(num) else "impar"

    print(f"El número {num} es {primo}, {fibo} y {par}.")

checker(10)
