# /*
# * Dada una URL con parámetros, crea una función que obtenga sus valores.
# * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
# *
# * Ejemplo: En la url https: // retosdeprogramacion.com?year = 2023 & challenge = 0
# * los parámetros serían["2023", "0"]
# */

import re

## Función que obtiene los parámetros de una URL usando expresiones regulares
def get_url_params(url):


    url_regex = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"

    if re.match(url_regex, url):
        params = re.findall(r"(\?|\&)([^=]+)\=([^&]+)", url)
        for match in params:
            print(
                f"parámetro: {match[1]} valor: {match[2]}")
    else:
        print("URL no válida.")
        regex = r"(\?|\&)([^=]+)\=([^&]+)"
        matches = re.findall(regex, url)

        for match in matches:
            print(f"parámetro: {match[1]} valor: {match[2]}")

## Ejemplo de uso

url = "https://retosdeprogramacion.com?year=2023&challenge=11&languaje=python"
get_url_params(url)

