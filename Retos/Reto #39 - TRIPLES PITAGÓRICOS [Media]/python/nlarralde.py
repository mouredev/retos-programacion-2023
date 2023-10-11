"""
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
"""


def buscar_terna(limite: int) -> list:

    ternas = []
    cuadrados = [pow(x, 2) for x in range(0, limite + 1)]

    for ind in range(1, cuadrados.__len__() - 2):

        for i in range(ind + 1, cuadrados.__len__()):

            resultado = cuadrados[ind] + cuadrados[i]
            if cuadrados.__contains__(resultado):
                ternas.append([ind, i, cuadrados.index(resultado)])

    return ternas


print(buscar_terna(10))
print(buscar_terna(100))
print(buscar_terna(1000))
