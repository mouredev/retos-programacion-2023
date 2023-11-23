# Reto #11: URL params
#### Dificultad: Fácil | Publicación: 13/03/23 | Corrección: 20/03/23

## Enunciado

"""
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
"""

url = input("Pegue su url con parámetros: ")


def findParams():
    params = []
    x = url.split("?")
    lista = x[1].split("&") # ['year=2023', 'challenge=0']
    for y in lista:
        z = y.split("=") # ['year', '2023']
        params.append(z[1])

    return params

params_url = findParams()
print(f"los parámetros de la url son: {params_url}")
