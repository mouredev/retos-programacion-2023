#  * Crea una función que encuentre todas las combinaciones de los números
#  * de una lista que suman el valor objetivo.
#  * - La función recibirá una lista de números enteros positivos
#  *   y un valor objetivo.
#  * - Para obtener las combinaciones sólo se puede usar
#  *   una vez cada elemento de la lista (pero pueden existir
#  *   elementos repetidos en ella).
#  * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
#  *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
#  *   (Si no existen combinaciones, retornar una lista vacía)
#  */
import numpy as np


#defino una función que me de todas las combinaciones de indices posibles sin repetir ni alterar el orden
def combinador_de_indices(lista_de_indices,combinaciones=[]):
    largo_inicial=len(combinaciones)
    if largo_inicial==0:
        combinaciones.append(lista_de_indices)

    if len(lista_de_indices)>1:
        for i in range(len(lista_de_indices)):
            if not(lista_de_indices[:i]+lista_de_indices[i+1:] in combinaciones):
                combinaciones.append(lista_de_indices[:i]+lista_de_indices[i+1:])

        for i in range(largo_inicial,len(combinaciones)):
            combinador_de_indices(combinaciones[i],combinaciones=combinaciones)

    return combinaciones


#funcion auxiliar para dado un array y un array de indices, devolver los valores del array en los indices dados
def ind_to_values(valores,indices):
    valor=[]
    for i in indices:
        valor.append(valores[i])
    return valor



def las_sumas(lista,obj):
    resultado=[]

    combinaciones=combinador_de_indices(  list( range(len(lista)))  )  #creo todas las combinaciones de indices posibles
           
    for comb in combinaciones:
        if np.sum(ind_to_values(lista,comb))==obj:  #revisa si la suma de los valores del array dan el objetivo
            resultado.append(ind_to_values(lista,comb))  #añado el array al resultado

    return resultado


print(las_sumas([1,5,3,2], 6))
print(las_sumas([0,3,2,5,2,10], 10))

# print(las_sumas([1,5,2,3], 6))
