'''
Crea una función que encuentre todos los triples pitagóricos
(ternas) menores o iguales a un número dado.
- Debes buscar información sobre qué es un triple pitagórico.
- La función únicamente recibe el número máximo que puede
  aparecer en el triple.
- Ejemplo: Los triples menores o iguales a 10 están
  formados por (3, 4, 5) y (6, 8, 10).
'''

def find_pitagoric_triplet(max_n):
    if max_n <= 0:
        return 'Max N debe ser mayor que 0'
    
    triplets = []
    for a in range(1, max_n + 1):
        for b in range(a, max_n + 1):
            for c in range(b, max_n + 1):
                if a**2 + b**2 == c**2:
                    triplets.append((a, b, c))
    return triplets

print('Tripletas pitagoricas por debajo de 10:')
print(find_pitagoric_triplet(10))

print('Tripletas pitagoricas por debajo de 50:')
print(find_pitagoric_triplet(50))

print('Tripletas pitagoricas por debajo de -1:')
print(find_pitagoric_triplet(-1))