# /*
#  * Dada una URL con parámetros, crea una función que obtenga sus valores.
#  * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#  *
#  * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#  * los parámetros serían ["2023", "0"]
#  */

def get_params(url):
    url = url.split("?")[1]
    url = url.split("&")
    return [param.split("=")[1] for param in url]
print(get_params("https://retosdeprogramacion.com?year=2023&challenge=0")) # ["2023", "0"]