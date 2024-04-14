#!/usr/bin/python3

"""
# Reto #19: Análisis de texto
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


def procesar_texto(texto_entrada):

    numero_palabras = 0
    palabra_actual = []
    palabra_mas_larga = ""
    longitud_palabra_mas_larga = 0
    
    numero_oraciones = 0
    oracion_actual = []
    oracion_mas_larga = ""
    longitud_oracion_mas_larga = 0
    

    texto_entrada[-1] == "."
    texto_entrada += '.'

    # este es el unico bucle
    for c in texto_entrada:

        if c == '\n':
            continue

        if c == ' ':
            if len(palabra_actual):
                numero_palabras += 1
                if len(palabra_actual) > longitud_palabra_mas_larga:
                    palabra_mas_larga = "".join(palabra_actual)
                    longitud_palabra_mas_larga = len(palabra_mas_larga)
            palabra_actual = []
            oracion_actual.append(c)
            continue

        if c == '.':
            if len(palabra_actual):
                numero_palabras += 1
                if len(palabra_actual) > longitud_palabra_mas_larga:
                    palabra_mas_larga = "".join(palabra_actual)
                    longitud_palabra_mas_larga = len(palabra_mas_larga)
            if len(oracion_actual):
                numero_oraciones += 1
                if len(oracion_actual) > longitud_palabra_mas_larga:
                    oracion_mas_larga = "".join(oracion_actual)
                    longitud_oracion_mas_larga = len(oracion_mas_larga)
            palabra_actual = []
            oracion_actual = []
            continue

        oracion_actual.append(c)

        if c.isalpha():
            palabra_actual.append(c)


    print("numero_palabras:", numero_palabras)
    print("palabra_mas_larga:", palabra_mas_larga)

    print("numero_oraciones:", numero_oraciones)
    print("oracion_mas_larga:", oracion_mas_larga)

    print("palabras por oracion: ", "{:.2f}".format(numero_palabras/numero_oraciones))



if __name__ == '__main__':
    TEXTO = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna 
        aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
        ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit 
        esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
        occaecat cupidatat non proident, sunt in culpa qui officia 
        deserunt mollit anim id est laborum."""
    procesar_texto(TEXTO)

