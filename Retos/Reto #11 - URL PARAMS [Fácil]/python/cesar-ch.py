"""
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
"""
import re


def getParamsUrl(url):
    arr = re.findall(r'\=\w+', url)
    new_arr = []
    for i in arr:
        new_arr.append(i.split('=')[1])

    return new_arr


print(getParamsUrl('https://retosdeprogramacion.com?year=2023&challenge=0'))
