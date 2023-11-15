def sumaObjetivo(numeros:list, objetivo:int):
    """
    Encuentra todas las combinaciones de los números de una 
    lista que suman el valor objetivo.

    Args:
    - numeros (list): Lista de numeros, enteros positivos, de la que quiero 
    encontrar las combinaciones.
    - objetivo (int): Valor entero positivo objetivo.
    Returns:
    - combinaciones (list): Lista con las combinaciones encontradas.
    """
    # Caso base de la recursión (que la suma de la lista sea el numero)
    if sum(numeros) == objetivo:
        return [numeros]
    
    # Defino la lista donde guardadaré las combinaciones
    combinaciones = []

    for i in range(len(numeros)):
        # Evaluo cada lista posible
        resto_numeros = numeros[:i] + numeros[i+1:]
        # Encuentro las listas que cumplen
        combinaciones_resto = sumaObjetivo(resto_numeros, objetivo)

        # Para cada combinacion encontrada, si no está en las combinaciones, la añado
        # el if lo aplico para evitar listas repetidas
        for combinacion in combinaciones_resto: 
            if combinacion not in combinaciones:
                combinaciones.append(combinacion) 

    return combinaciones

resultado = sumaObjetivo([1, 5, 3, 2, 3, 6], 6)
print(f"Soluciones: {resultado}")