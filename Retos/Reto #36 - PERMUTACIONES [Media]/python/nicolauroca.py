#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================#
#                      Información                        #
#=========================================================#

'''
/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */
'''

#=========================================================#
#                        Módulos                          #
#=========================================================#
# Ninguno

#=========================================================#
#                   Variables Globales                    #
#=========================================================#
# Ninguna

#=========================================================#
#                        Funciones                        #
#=========================================================#

def permutaciones(palabra, inicio = 0):
    """
    Genera todas las permutaciones únicas de una palabra dada.

    Esta función utiliza un enfoque recursivo para generar todas las permutaciones posibles de los caracteres
    en la palabra de entrada. Las permutaciones se almacenan en un conjunto (set) para garantizar que solo se
    incluyan permutaciones únicas.

    Args:
        palabra (str): La palabra de entrada para la cual se generarán las permutaciones.
        inicio (int, opcional): El índice de inicio para la generación de permutaciones. No es necesario
        especificarlo al llamar a la función.

    Returns:
        set: Un conjunto que contiene todas las permutaciones únicas de la palabra de entrada.

    Ejemplo:
        >>> resultado = permutaciones("abcd")

    Notas:
        - Esta función puede ser lenta para palabras muy largas debido a su enfoque recursivo.
        - Se recomienda su uso con palabras de longitud razonable.

    """
    # Verificamos si la palabra es una lista (si no, convertimos)
    if not isinstance(palabra, list):
        palabra = list(palabra)

    # Preparamos la salida. Dado que queremos que solo contenga valores únicos, usamos un conjunto (set)
    salida = set()

    # Jugamos con la longitud restante para saber si añadimos o seguimos con la recursión
    if inicio == len(palabra) - 1:
        salida.add(''.join(palabra))
 
    else:
        for i in range(inicio, len(palabra)):
            # Jugamos por elemento (letra) de la palabra
            palabra[inicio], palabra[i] = palabra[i], palabra[inicio]

            # Se podría usar un bucle jugando con las posiciones, veo más cómoda la recursividad
            salida.update(permutaciones(palabra, inicio + 1))

            # Dejamos el texto como estaba
            palabra[inicio], palabra[i] = palabra[i], palabra[inicio]

    return salida



#=========================================================#
#                         Código                          #
#=========================================================#

if __name__ == '__main__':
	print(permutaciones('sol'))