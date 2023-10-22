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



def triples_pitagoricos(maximo: int) -> list:
    """Triples Pitagóricos son tres números enteros a, b y c que satisfacen la ecuación del teorema de Pitágoras: ( a2 + b2 = c2 )

    Args:
        maximo (int): Numero máximo a anaalizar

    Returns:
        list: Lista de los trios pitagóricos
    """
    resultado = []
    for a in range(maximo, 0, -1):
        for b in range(maximo, 0, -1):
            for c in range(maximo, 0, -1):
                if pow(a, 2) + pow(b, 2) == pow(c, 2):
                    print(f'{(a, b, c)}: {pow(a, 2) + pow(b, 2)} ({pow(a, 2)} + {pow(b, 2)}) = {pow(c, 2)}')
                    resultado.append((a, b, c))
    return resultado

print(triples_pitagoricos(10))
