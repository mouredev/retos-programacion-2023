# * Dada una URL con parámetros, crea una función que obtenga sus valores.
# * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
# *
# * Ejemplo: En la url https: // retosdeprogramacion.com?year = 2023 & challenge = 0
# * los parámetros serían["2023", "0"]

def obtenerValoresURL(url: str):
    variables = []
    try:
        variablesEnURL = url.split("?")[1]
        for v in variablesEnURL.split("&"):
            variables.append(v.split("=")[1])
        print(variables)
    except:
        print("Esa URL no tiene parámetros los cuáles desglosar")


obtenerValoresURL("https://retosdeprogramacion.com") 
obtenerValoresURL("https://retosdeprogramacion.com?year=2023&challenge=0")