#1- Generamos todos las combinaciones posibles de los elementos de la lista con recursividad
#2- Filtro de la lista generada solo los que suman como el valor objetivo

def combinaciones_posibles(lista_numeros):
    return combinaciones_posibles_recursivas([], lista_numeros)

def combinaciones_posibles_recursivas(actual, lista_numeros):
    if lista_numeros != []:
        return combinaciones_posibles_recursivas(actual, lista_numeros[1:]) + combinaciones_posibles_recursivas(actual + [lista_numeros[0]], lista_numeros[1:])
    return [actual]

def filtrar_segun_sumatoria(lista_de_combinaciones, valor):
    lista_filtrada = []
    for i in lista_de_combinaciones:
        if sum(i) == valor:
            lista_filtrada.append(i)
    return lista_filtrada

lista_numeros = [1, 5, 3, 2]
valor_objetivo = 5
combinaciones = combinaciones_posibles(lista_numeros)
resultado = filtrar_segun_sumatoria(combinaciones, valor_objetivo)

print(resultado)


