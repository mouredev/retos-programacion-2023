"""
/*
* Dada una URL con parámetros, crea una función que obtenga sus valores.
* No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
*
* Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
* los parámetros serían ["2023", "0"]
*/
"""

def url_params(url):
    parameters = []

    url_parameters = url.split("?")
    print(url_parameters)

    url_parameters.remove(url_parameters[0])
    url_parameters = "".join(url_parameters).split("&")
    print(url_parameters)

    for param,values in enumerate(url_parameters):
        for value in values:
            if value == "=":
                parameters.append(values[values.index(value)+1::])
    print(parameters)

url_params("https://retosdeprogramacion.com?year=2023&challenge=0")