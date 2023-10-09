def find_sum(lista, target):
    combinaciones=[]
    encontrado=[]
    listaCopy=[]
    suma=0
    lista.sort()
    for i, v in enumerate(lista):
        suma=sum(lista)#Suma toda la lista
        combinaciones.append(lista) if suma==target else None  #si la suma de la lista es igual al target la agrega a las combinaciones        
#----------------------------------------------------------------------------------------------------------------------------------
        listaCopy=lista.copy()
        listaCopy.pop(i)#A la copia de la lista le quitamos el elemento para ir reduciendo la lista y seguir con otra combinacion
        encontrado=find_sum(listaCopy,target)#Al volver a llamar la funcion sumara la lista estara reducida para comprobar otra combinacion
#Aqui se detiene la funcion hasta que termine la recursion--------------------------------------------------------------------------------------
        if encontrado != []:#si el resultado no esta vacio
            for elemento in encontrado:#Por cada elemento encontrado y
                if elemento not in combinaciones:#si no esta en la combinaciones
                    combinaciones.append(elemento)#Se agrega a combinaciones
        
    return combinaciones

lista=[1, 5, 3, 2]
lista2=[1,2,2,1,3,4,-1]
lista3=[1,7]

print(find_sum(lista, 6))
print(find_sum(lista2, 4))
print(find_sum(lista3, -1))