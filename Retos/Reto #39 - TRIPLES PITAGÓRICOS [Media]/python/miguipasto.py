# /*
#  * Crea una función que encuentre todos los triples pitagóricos
#  * (ternas) menores o iguales a un número dado.
#  * - Debes buscar información sobre qué es un triple pitagórico.
#  * - La función únicamente recibe el número máximo que puede
#  *   aparecer en el triple.
#  * - Ejemplo: Los triples menores o iguales a 10 están
#  *   formados por (3, 4, 5) y (6, 8, 10).
#  */

def tripletes_pitagoricos(max: int):
    tripletes = []
    for a in range(1, max + 1):
        for b in range(a, max + 1):
            c_cuadrado = a**2 + b**2
            c = int(c_cuadrado**0.5)
            if c <= max and c_cuadrado == c**2:
                tripletes.append((a, b, c))
    return tripletes

resultados = tripletes_pitagoricos(10)
print("Los tripletes pitagóricos son:",resultados)