#!/usr/bin/python3

"""
# Reto #9: Heterograma, isograma y pangrama
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
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


from collections import Counter
from string import ascii_lowercase
from unidecode import unidecode


def convert_ascii(cadena):
    cadena2 = "".join([ (unidecode(item) if item != "ñ" else item) for item in cadena ])
    return cadena2


def preprocesar_cadena(cadena):
    cadena = "".join([ item for item in cadena if item.isalpha() ])
    cadena = cadena.lower()
    cadena = convert_ascii(cadena)
    return cadena


def esHeterograma(cadena, preproc=False):
    if not preproc:
        cadena = preprocesar_cadena(cadena)
    for item in cadena:
        if cadena.count(item) > 1:
            return False
    return True


def esPangrama(cadena, preproc=False):
    if not preproc:
        cadena = preprocesar_cadena(cadena)
    for alc in ascii_lowercase:
        if not alc in cadena:
            return False
    if not "ñ" in cadena:
        return False
    return True
    

def esIsograma(cadena, preproc=False):
    if not preproc:
        cadena = preprocesar_cadena(cadena)
    counts = dict(Counter(cadena))
    count_values = list(counts.values())
    for item in count_values:
        if item != count_values[0]:
            return False
    return True


if __name__ == '__main__':

    ejemplos = [    
        "José compró una vieja zampoña en Perú. Excusándose, Sofía tiró su whisky al desagüe de la banqueta.", 
        "El cadáver de Wamba, rey godo de España, fue exhumado y trasladado en una caja de zinc que pesó un kilo.", 
        "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.", 
        "El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado un saxofón.", 
        "Jovencillo emponzoñado de whisky: ¡qué figurota exhibe!", 
        "Quiere la boca exhausta vid, kiwi, piña y fugaz jamón.", 
        "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.", 
        "El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.", 
        "El jefe buscó el éxtasis en un imprevisto baño de whisky y gozó como un duque.", 
        "Le gustaba cenar un exquisito sándwich de jamón con zumo de piña y vodka frío.", 
        "Es extraño mojar queso en la cerveza y probar whisky de garrafa.", 
        "Bebo whisky porque extraño mi loca juventud fugaz.", 
        "yuxtaponer", 
        "centrifugado", 
        "luteranismo", 
        "adulterinos", 
        "hiperblanduzcos", 
        "acondicionar", 
        "escritura", 
        "intestinos", 
        "papelera", 
    ]

    for cadena in ejemplos:
        print("TEXTO:", f'"{cadena}"')
        bandera_pangrama = esPangrama(cadena)
        print("Es Pangrama: ", "SI" if bandera_pangrama else "NO")
        bandera_heterograma = esHeterograma(cadena)
        print("Es heterograma: ", "SI" if bandera_heterograma else "NO")
        bandera_isograma = esIsograma(cadena)
        print("Es Isograma: ", "SI" if bandera_isograma else "NO")
        print()
        