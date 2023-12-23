"""
/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */
"""

from itertools import combinations

def combinations_of_three(numbers):
  return combinations(numbers, 3)

maxim_pitagoric = input("Introduce el número máximo que puede aparecer en el triple pitagórico:  ")
numbers = list(range(1, int(maxim_pitagoric) + 1))
for combination in combinations_of_three(numbers):
  a, b, c = list(combination)
  if ((a**2 + b**2) == c**2):
    print(f"({a}, {b}, {c})")
  if ((a**2 + c**2) == b**2):
    print(f"({a}, {b}, {c})")
  if ((b**2 + c**2) == a**2):
    print(f"({a}, {b}, {c})")
