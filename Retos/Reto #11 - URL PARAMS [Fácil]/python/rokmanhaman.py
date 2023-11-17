"""
Reto #11: URL PARAMS
FÁCIL | Publicación: 13/03/23 | Resolución: 20/03/23
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
"""

def split_url(url):
    url_p0 = url.split("?")[0]
    url_p1 = url.split("?")[1]
    parametrs = url_p1.split("&")
    my_dict = {param.split("=")[0]: param.split("=")[1] for param in parametrs}

    return my_dict.values() 


url = "https://retosdeprogramacion.com?year=2023&challenge=0&activo=true&visible=false&pag=42&q=consulta"
s = split_url(url)
print(s)
