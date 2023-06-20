url = "https://retosdeprogramacion.com?year=2023&challenge=0&category=1&level=2&language=1&author=1&order=1&sort=1&search="

def sacar_parametros(url):
    url_partida = url.split("?")[1]
    lista_parametros = []
    if url_partida == -1:
        return lista_parametros
    

    indice_igual = url_partida.find("=")
    indice_and = url_partida.find("&")

    while len(url_partida) > 0:
        if indice_and == -1: # Si no hay más parámetros
            lista_parametros.append(url_partida[indice_igual + 1:])
            url_partida = ""

            indice_igual = url_partida.find("=")
            indice_and = url_partida.find("&")
        else:
            lista_parametros.append(url_partida[indice_igual + 1:indice_and])
            url_partida = url_partida[indice_and + 1:]

            indice_igual = url_partida.find("=")
            indice_and = url_partida.find("&")


    return lista_parametros
    
    
            


print(sacar_parametros(url))