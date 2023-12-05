"""
Reto #39: TRIPLES PITAGÓRICOS
MEDIA | Publicación: 02/10/23 | Resolución: 09/10/23
/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */
 Tres números enteros a , b , c que satisfacen la ecuación del teorema
 de Pitágoras ( a2 + b2 = c2 ) son llamados triples Pitagóricos
"""

def triple_pitagorico(c_max):
    
    result = []

    for c in range(1, c_max+1, 1):
        for b in range(1, c+1, 1):
            for a in range(1, b+1, 1):
                if c ** 2 == a ** 2 + b ** 2:
                    result.append((a,b,c))

    return result

pita = triple_pitagorico(19)

print(pita)

