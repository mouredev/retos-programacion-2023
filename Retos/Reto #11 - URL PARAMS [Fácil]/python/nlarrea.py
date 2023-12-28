"""
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
"""

def getParameters(url):
    try:
        index = url.index('?')
    except ValueError:
        return "No hay parámetros"

    if index == (len(url) - 1):
        return "No hay parámetros"
    
    parameters = url[url.index('?') + 1 : ]


    def getValues(params):
        try:
            params.index('&')
        except ValueError:
            # se ejecuta cuando no hay más parámetros
            value = params[params.index('=') + 1 : ]
            params = ""
        else:
            # se ejecuta siempre que haya más parámetros
            value = params[params.index('=') + 1 : params.index('&')]
            params = params[params.index('&') + 1 : ]

        return [params, value]


    values = []

    while True: #(parameters.index('=') != -1):
        try:
            [parameters, value] = getValues(parameters)
            values.append(value)
        except ValueError:
            break

    if len(values) == 1 and values[0] == "":
        return "Los parámetros no están definidos"

    return values


print(getParameters("https://retosdeprogramacion.com?year=2023&challenge=0"))     # ['2023', '0']
print(getParameters("https://retosdeprogramacion.com"))                           # No hay parámetros
print(getParameters("https://retosdeprogramacion.com?"))                          # No hay parámetros
print(getParameters("https://retosdeprogramacion.com?year=2023"))                 # ['2023']
print(getParameters("https://retosdeprogramacion.com?year=2023&"))                # ['2023']
print(getParameters("https://retosdeprogramacion.com?year=&"))                    # Los parámetros no están definidos