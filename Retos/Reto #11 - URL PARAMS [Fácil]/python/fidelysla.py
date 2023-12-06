
# * Dada una URL con parámetros, crea una función que obtenga sus valores.
# * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
# *
# * Ejemplo: En la url https: // retosdeprogramacion.com?year = 2023 & challenge = 0
# * los parámetros serían["2023", "0"]


url = "https://retosdeprogramacion.com?year=2023&challenge=0"


def getParametersValues(url):
    parameters = url.split("?")[1]
    parameters_key_and_value = parameters.split("&")
    parameters_values = list()
    for l in parameters_key_and_value:
        parameters_values.append(l.split("=")[1])
    return parameters_values


print(getParametersValues(url))
