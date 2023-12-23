'''/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
a=m^2 - n^2 , b=2mn y c=m^2 + n^2 .

Por ejemplo, si m=4 y n=3 entonces,

a=4 2 – 3 2 =16 – 9=7
b=2 × 4 × 3=24
c=4 2 + 3 2 =16 + 9=25
Usando la ecuación a^2 + b^2 =c^2
 */'''

def triple_pitagorico(max):
    triples = []
    for m in range(2, max + 1):
        for n in range(1, m):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if c <= max:
                triples.append([a, b, c])
    return triples
max = 10
solution = triple_pitagorico(max)
print(*solution)