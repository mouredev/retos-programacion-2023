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

def is_prime_twin(number: int ) -> bool:
    if is_prime(number) and is_prime(number + 2):
        return True
    else:
        return False


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True
    
print(is_prime_twin(3))
print(is_prime_twin(5))
print(is_prime_twin(11))
print(is_prime_twin(17))
print(is_prime_twin(29))
print(is_prime_twin(41))
print('-------------------')
print(is_prime_twin(7))
print(is_prime_twin(13))
print(is_prime_twin(19))
print(is_prime_twin(23))
print(is_prime_twin(31))
print(is_prime_twin(37))
