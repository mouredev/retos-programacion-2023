# Crea una función que encuentre todos los triples pitagóricos
# (ternas) menores o iguales a un número dado.
# - Debes buscar información sobre qué es un triple pitagórico.
# - La función únicamente recibe el número máximo que puede
# aparecer en el triple.
# - Ejemplo: Los triples menores o iguales a 10 están
# formados por (3, 4, 5) y (6, 8, 10).

import math

def find_tri_pitagoras(max: int) -> list:

    result = []
    
    def calcular_catetos(hipotenusa):
        # Iteramos sobre todos los números enteros desde 1 hasta la mitad de la hipotenusa
        for a in range(1, hipotenusa):
            # Calculamos b usando el teorema de Pitágoras
            b = math.sqrt(hipotenusa**2 - a**2)
            
            # Verificamos si b es un número entero (es decir, un número sin decimales)
            if b.is_integer():
                return [a, int(b)]
        
        # Si no se encontraron catetos enteros, retornamos None
        return None

    for a in range(1, max + 1):
        b = calcular_catetos(a)
        # print(str(a) + '[' + str(b) + ']')
        if b is not None:
            result.append([b[0], b[1], a])
    
    return result


print(find_tri_pitagoras(10))
