"""
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
"""

def pythagorean_triples(max_num: int) -> list:
    # Check if correct data
    if type(max_num) != int:
        print("Given data must be a number")
        return []
    
    if max_num <= 1:
        print("Given number must be greater than 1")
        return []
    
    # Find pythagorean triples
    triples = []
    for a in range(1, max_num + 1):
        for b in range(a, max_num + 1):
            ab_squared = a**2 + b**2
            c = ab_squared**0.5

            if c > max_num:
                break

            if ab_squared == int(c)**2:
                triples.append((a, b, int(c)))

    return triples


print(pythagorean_triples(10))      # [(3, 4, 5), (6, 8, 10)]