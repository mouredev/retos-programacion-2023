# /*
#  * Crea una función que encuentre todos los triples pitagóricos
#  * (ternas) menores o iguales a un número dado.
#  * - Debes buscar información sobre qué es un triple pitagórico.
#  * - La función únicamente recibe el número máximo que puede
#  *   aparecer en el triple.
#  * - Ejemplo: Los triples menores o iguales a 10 están
#  *   forma
# dos por (3, 4, 5) y (6, 8, 10).
#  */
import math

def triples_pitagoricos(num_dado):
    resp = []
    for i in range(1,num_dado):
        for j in range(1,i):
            b = math.pow((math.pow(i,2) + math.pow(j,2)),0.5)
            if b > num_dado:
                break
            if b//1 == b:
                parc = (j,i,int(b))
                resp.append(parc)
            
    return resp

print(triples_pitagoricos(50))
