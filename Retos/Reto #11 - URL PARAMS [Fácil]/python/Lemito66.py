"""
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"] 
"""

def detect_parameters(url):
    parameters = []
    separate_ampersands = url.split("&") # Split a string into a list where each word is a list item:
    for separate_ampersand in separate_ampersands:
        if "=" in separate_ampersand:
            parameter = separate_ampersand.split("=")
            if len(parameter) == 2 and parameter[1] != "":
                parameters.append(parameter[1])
    return parameters

print(detect_parameters("https://retosdeprogramacion.com?year=2023&challenge=0&Lemito66=Fantastic"))