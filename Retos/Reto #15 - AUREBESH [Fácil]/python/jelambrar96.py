#!/usr/bin/python3

"""
# Reto #15: Aurebesh
/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
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

# import json

DICT_TO_AUREBEK_MONO = {
    "a": "aurebek",
    "c": "cresh",
    "j": "jenth",
    "k": "krill",
    "s": "senth",
    "t": "trill",
    "z": "zerek",
    "b": "besh",
    "d": "dorn",
    "f": "forn",
    "g": "grek",
    "h": "herf",
    "l": "leth",
    "m": "mern",
    "n": "nern",
    "p": "peth",
    "r": "resh",
    "w": "wesk",
    "x": "xesh",
    "y": "yirt",
    "e": "esk",
    "i": "isk",
    "o": "osk",
    "q": "qek",
    "u": "usk",
    "v": "vev"
}

DICT_AUREBECK_TWO = {
    "ch": "cherek",
    "kh": "krenth",
    "oo": "orenth",
    "eo": "onith",
    "th": "thesh",
    "ae": "enth",
    "sh": "shen",
    "ng": "nen"
}


def traducir_palabra_espanol_a_aurebesh(palabra):
    for k, v in DICT_AUREBECK_TWO.items():
        palabra = palabra.replace(k, v.upper())
    for k, v in DICT_TO_AUREBEK_MONO.items():
        palabra = palabra.replace(k, v.upper())
    return palabra.lower()


def traducir_palabra_aurebesh_a_espanol(palabra):
    for v, k in DICT_TO_AUREBEK_MONO.items():
        palabra = palabra.replace(k, v.upper())
    for v, k in DICT_AUREBECK_TWO.items():
        palabra = palabra.replace(k, v.upper())
    return palabra.lower()


if __name__ == '__main__':

    lista_palabras = [
        'industria', 'escribir', 'mientras', 'listo', 'exigir', 'buscar', 'parecer', 
        'primavera', 'causa', 'inventar', 'prisa', 'viajes', 'miedo', 'siglo', 
        'hacer', 'historia', 'particular,', 'llegar', 'nunca', 'fruta', 'suelo', 
        'llamada', 'desear', 'perro', 'movimiento', 'pista', 'querido', 'estrella', 
        'bastante', 'decir', 'dejar', 'diccionario', 'tratar']

    for item in lista_palabras:
        lower_item = item.lower()
        aurebeck_item = traducir_palabra_espanol_a_aurebesh(lower_item)
        espanol_item = traducir_palabra_aurebesh_a_espanol(aurebeck_item)
        print(lower_item, aurebeck_item, espanol_item, sep="\t-\t")


