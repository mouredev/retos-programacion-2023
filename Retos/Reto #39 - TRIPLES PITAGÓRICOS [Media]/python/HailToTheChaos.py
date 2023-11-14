'''
Crea una función que encuentre todos los triples pitagóricos
(ternas) menores o iguales a un número dado.
- Debes buscar información sobre qué es un triple pitagórico.
- La función únicamente recibe el número máximo que puede
  aparecer en el triple.
- Ejemplo: Los triples menores o iguales a 10 están
  formados por (3, 4, 5) y (6, 8, 10).

  a^2 + b^2 = c^2
  
'''


def find_pythagorean_triples(max: int) -> list:
    triples = []

    for a in range(1, max + 1):
        for b in range(a, max + 1):
            # c = (a^2 + b^2)^1/2
            c = (a ** 2 + b ** 2) ** 0.5
            # Tiene que ser numero entero y menor o igual al numero dado
            if c.is_integer() and c <= max:
                triples.append((a, b, int(c)))

    return triples


if __name__ == '__main__':
    print(find_pythagorean_triples(15))
