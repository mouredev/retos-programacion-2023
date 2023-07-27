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
 */
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(start, end):
    twin_primes = []
    for num in range(start, end):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

# Obtenemos el rango máximo del usuario
max_range = int(input("Ingrese el rango máximo: "))

# Encontramos los pares de números primos gemelos
result = find_twin_primes(3, max_range)

# Mostramos los pares encontrados
for twin_prime in result:
    print(twin_prime)