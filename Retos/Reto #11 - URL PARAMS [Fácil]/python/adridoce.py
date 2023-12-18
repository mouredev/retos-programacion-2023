"""
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
"""

def getParams(url):
    cadena_dividida = url.split("?", 1)[1]
    valores = cadena_dividida.split("&")

    for posicion in valores:
        print(posicion.split("=")[1])


getParams("https://retosdeprogramacion.com?year=2023&challenge=0")