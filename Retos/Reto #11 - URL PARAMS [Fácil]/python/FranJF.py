#
# Dada una URL con parámetros, crea una función que obtenga sus valores.
# No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#
# Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
# los parámetros serían ["2023", "0"]
#

def sacar_parametros_url(url:str):
    parametros:list = url.split("?")[1].split("&")
    valores:list = []
    for parametro in parametros:
        valor = parametro.split("=")[1]
        valores.append(valor)
    return valores

print(sacar_parametros_url("https://retosdeprogramacion.com?year=2023&challenge=0"))
