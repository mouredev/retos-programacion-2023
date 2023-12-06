import re

def obtener_parametros(url):
    parametros = []
    cadena_dividida = url.split("?")
    #print(cadena_dividida)

    cadena_valores = cadena_dividida[1].split("&")
    #print(cadena_valores)

    for valores in cadena_valores:
        valor = valores.split("=")[1]
        parametros.append(valor)
    print(parametros)

obtener_parametros("https://retosdeprogramacion.com?year=2023&challenge=0")
obtener_parametros("https://rickandmortyapi.com/api/character/?page=2")
obtener_parametros("https://rickandmortyapi.com/api/character/?name=rick&status=alive")