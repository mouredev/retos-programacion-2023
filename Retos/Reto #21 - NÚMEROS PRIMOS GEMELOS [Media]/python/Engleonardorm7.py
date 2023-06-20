# * Crea un programa que encuentre y muestre todos los pares de números primos
#  * gemelos en un rango concreto.
#  * El programa recibirá el rango máximo como número entero positivo.
#  * 
#  * - Un par de números primos se considera gemelo si la diferencia entre
#  *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#  *
#  * - Ejemplo: Rango 14
#  *   (3, 5), (5, 7), (11, 13)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(range_max):
    twin_primes = []
    for n in range(2, range_max):
        if is_prime(n) and is_prime(n + 2):
            twin_primes.append((n, n + 2))
    return twin_primes

range_max = int(input("Ingresa el rango máximo: "))
twin_prime_pairs = find_twin_primes(range_max)

print("Pares de números primos gemelos en el rango hasta", range_max, ":")
for pair in twin_prime_pairs:
    print(pair)
