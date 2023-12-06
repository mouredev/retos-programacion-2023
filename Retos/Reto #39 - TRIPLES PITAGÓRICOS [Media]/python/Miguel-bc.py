'''

/*
* Crea una función que encuentre todos los triples pitagóricos
* (ternas) menores o iguales a un número dado.
* - Debes buscar información sobre qué es un triple pitagórico.
* - La función únicamente recibe el número máximo que puede
*   aparecer en el triple.
* - Ejemplo: Los triples menores o iguales a 10 están
*   formados por (3, 4, 5) y (6, 8, 10).
*/

'''
 
import math
 
def combinaciones(numero):
    lista = []
    for i in range(1, numero):        
        for n in range(i, numero):   
            combinacion = [i,n+1]
            lista.append(combinacion)   
    return lista

nmax = int(input("Numero máximo: "))

catetos = combinaciones(nmax)
resultados = list(range(1,nmax+1))

triples =[]

for elemento in catetos:    
    hipotenusacuadrado = math.pow(elemento[0],2) + math.pow(elemento[1],2)
    hipotenusa = math.sqrt(hipotenusacuadrado)
    if hipotenusa in resultados:
        triples.append([elemento[0],elemento[1],hipotenusa])
  
print(triples)           
    


 
 
 
