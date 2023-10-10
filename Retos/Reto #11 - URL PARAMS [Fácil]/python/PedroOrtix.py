def extraer_parametros(url):
    parametros = {}
    url = url.split("?")
    if len(url) > 1:
        url = url[1]
        url = url.split("&")
        for i in url:
            i = i.split("=")
            parametros[i[0]] = i[1]
    return parametros

URL = "https://retosdeprogramacion.com?year=2023&challenge=0"
print(extraer_parametros(URL)) # {'year': '2023', 'challenge': '0'}