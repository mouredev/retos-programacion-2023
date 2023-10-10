'''
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
'''

def pitagoras(n):
    print("Los triples menores o iguales a",n,"son:")
    for a in range(1, n+1):
        for b in range(a, n+1):
            cCuadrado = a**2 + b**2
            c = int(cCuadrado ** 0.5)
            if c**2 == cCuadrado and c <= n:
                print("(", a, ",", b, ",", c, ")")

pitagoras(20)
'''
3,4,5
5,12,13
6,8,10
8,15,17
9,12,15
12,16,20
'''
pitagoras(10)
'''
3,4,5
6,8,10
'''
pitagoras(5)
'''
3,4,5
'''