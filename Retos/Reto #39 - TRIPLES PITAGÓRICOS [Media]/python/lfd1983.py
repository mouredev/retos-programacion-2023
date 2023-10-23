# /*
#  * Crea una función que encuentre todos los triples pitagóricos
#  * (ternas) menores o iguales a un número dado.
#  * - Debes buscar información sobre qué es un triple pitagórico.
#  * - La función únicamente recibe el número máximo que puede
#  *   aparecer en el triple.
#  * - Ejemplo: Los triples menores o iguales a 10 están
#  *   formados por (3, 4, 5) y (6, 8, 10).
#  */

def triples_pitagoricos(n):
    resultado = []
    for c in range(1,n+1): 
        for b in range(1,c+1):       
          for a in range(1,b+1):
              if a**2+b**2 == c**2:
                  resultado.append([a,b,c])
    return resultado

print(triples_pitagoricos(50))