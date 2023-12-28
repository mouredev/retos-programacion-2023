"""
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
"""


def get_pairs_of_primes(range_of_numbers):
    pairs_of_primes = []
    pair = []

    for i in range(range_of_numbers + 1):
        if is_prime(i):
            pair.append(i)

            if len(pair) == 2:
                if pair[1] - pair[0] == 2:
                    pairs_of_primes.append(tuple(pair))
            
                pair.pop(0)

    return pairs_of_primes


def is_prime(number):
    if number < 2: return False
    
    for i in range(2, number):
        if number % i == 0: return False

    return True


def print_pairs(pairs):
    print("\nPairs of prime numbers:")
    for pair in pairs:
        print(pair)


print_pairs(get_pairs_of_primes(14))