# Reto #39: Triples pitagóricos
#### Dificultad: Media | Publicación: 02/10/23 | Corrección: 09/10/23

## Enunciado

#
# Crea una función que encuentre todos los triples pitagóricos
# (ternas) menores o iguales a un número dado.
# - Debes buscar información sobre qué es un triple pitagórico.
# - La función únicamente recibe el número máximo que puede
#   aparecer en el triple.
# - Ejemplo: Los triples menores o iguales a 10 están
#   formados por (3, 4, 5) y (6, 8, 10).
#


class PythagoreanTriplesFinder:
    def __init__(self, maximum):
        self.maximum = maximum
        self.triples = []

    def find_pythagorean_triples(self):
        for a in range(1, self.maximum + 1):
            for b in range(a, self.maximum + 1):
                c_square = a ** 2 + b ** 2
                c = int(c_square ** 0.5)
                if c <= self.maximum and c_square == c ** 2:
                    self.triples.append((a, b, c))

    def get_triples(self):
        return self.triples

# Example usage:
max_value = 20
triples_finder = PythagoreanTriplesFinder(max_value)
triples_finder.find_pythagorean_triples()
triples = triples_finder.get_triples()
print(triples)

