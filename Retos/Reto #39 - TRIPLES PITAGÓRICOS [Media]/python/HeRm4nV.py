'''
Crea una función que encuentre todos los triples pitagóricos
  (ternas) menores o iguales a un número dado.
  - Debes buscar información sobre qué es un triple pitagórico.
  - La función únicamente recibe el número máximo que puede
    aparecer en el triple.
  - Ejemplo: Los triples menores o iguales a 10 están
   formados por (3, 4, 5) y (6, 8, 10).
'''

import math 
 
def pitagoric_numbers(number):
    triples = []
    for a in range(1, number):
        for b in range(a, number+1):
            if math.sqrt(a**2+b**2) <= number and math.sqrt(a**2+b**2).is_integer():
                triples.append([a,b, int(math.sqrt(a**2+b**2)) ])
    return triples


print(pitagoric_numbers(100))