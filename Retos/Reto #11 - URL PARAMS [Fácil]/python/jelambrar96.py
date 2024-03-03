#!/usr/bin/python3

"""
# Reto #11: URL params
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
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

import json

def getParams(url):
    cadena_dividida = url.split("?", 1)[1]
    valores = cadena_dividida.split("&")
    dict_params = dict([ tuple(item.split("=", 1)) for item in valores if item])
    return dict_params

if __name__ == '__main__':
    url = "https://retosdeprogramacion.com?year=2023&challenge=0"
    params = getParams(url)
    print(json.dumps(params, indent=4))
