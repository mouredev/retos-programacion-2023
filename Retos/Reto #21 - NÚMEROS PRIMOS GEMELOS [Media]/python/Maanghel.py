"""
Crea un programa que encuentre y muestre todos los pares de números primos
gemelos en un rango concreto.
El programa recibirá el rango máximo como número entero positivo.

- Un par de números primos se considera gemelo si la diferencia entre
    ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)

- Ejemplo: Rango 14
    (3, 5), (5, 7), (11, 13)
"""

import math

def find_pair_prime(num: int) -> list[tuple[int, int]]:
    """
    Encuentra todos los pares de números primos gemelos hasta un rango dado.

    Un número primo gemelo es aquel que forma pareja con otro primo cuya
    diferencia es exactamente 2.

    Args:
        num (int): Número entero positivo que define el límite superior del rango.

    Returns:
        List[Tuple[int, int]]: Lista de tuplas con los pares de primos gemelos encontrados.

    Raises:
        TypeError: Si el valor proporcionado no es un entero.
        ValueError: Si el número es menor que 2.

    Examples:
        >>> find_pair_prime(14)
        [(3, 5), (5, 7), (11, 13)]
    """

    if not isinstance(num, int):
        raise TypeError("El rango debe ser un número entero positivo.")
    if num < 2:
        raise ValueError("El rango debe ser mayor o igual a 2.")

    def is_prime(number: int) -> bool:
        """Verifica si un número es primo."""
        if number < 2:
            return False
        elif number == 2:
            return True
        elif number % 2 == 0:
            return False
        return all(number % i != 0 for i in range(3, math.isqrt(number) + 1, 2))

    prime_numbers = [i for i in range(2, num + 1) if is_prime(i)]

    pairs_prime = []
    for i, prime in enumerate(prime_numbers[:-1]):
        if prime_numbers[i + 1] - prime == 2:
            pairs_prime.append((prime, prime_numbers[i + 1]))

    return pairs_prime


if __name__ == "__main__":
    for pair in find_pair_prime(14):
        print(pair)
