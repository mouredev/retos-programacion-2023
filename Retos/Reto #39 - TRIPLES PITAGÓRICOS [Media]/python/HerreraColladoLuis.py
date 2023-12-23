#/*
# * Crea una función que encuentre todos los triples pitagóricos
# * (ternas) menores o iguales a un número dado.
# * - Debes buscar información sobre qué es un triple pitagórico.
# * - La función únicamente recibe el número máximo que puede
# *   aparecer en el triple.
# * - Ejemplo: Los triples menores o iguales a 10 están
# *   formados por (3, 4, 5) y (6, 8, 10).
# */

def is_triple(triple: list) -> bool:

    if len(triple) == 3:
        return triple[0]*triple[0] + triple[1]*triple[1] == triple[2]*triple[2]


def find_triples(max: int) -> list:

    numbers: list = []
    for i in range(1, max+1):
        numbers.append(i)

    # función recursiva
    def find_triple(start: int, triple: list):

        # triple encontrado
        if (is_triple(triple)):
            triples.append(triple[:])
            return

        # ningún triple más encontrado
        if start > max:
            return

        # backtrack
        for index in range(start, len(numbers)):

            if index > start and numbers[index] == numbers[index-1]:
                continue

            triple.append(numbers[index])
            find_triple(index + 1, triple)
            triple.pop()

    triples: list = []
    find_triple(0, [])
    return triples

print(find_triples(10))
