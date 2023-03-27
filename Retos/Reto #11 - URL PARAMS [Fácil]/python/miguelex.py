def FindParameters(url):

    params = []

    urlDividida = url.split("?")

    if len(urlDividida) > 1:
        listaParams = urlDividida[1].split("&")

        for param in listaParams:
            clearParam = param.split("=")
            if len(clearParam) > 1 and clearParam[1] != "":
                params.append(clearParam[1])
            else:
                return "La cadena no tiene parametros validos"

        return params
    else:
        return "La cadena no tiene parametros"


print(FindParameters("https://retosdeprogramacion.com?year=2023&challenge=0"))
print(FindParameters("https://retosdeprogramacion.com"))
print(FindParameters("https://retosdeprogramacion.com?"))
print(FindParameters("https://retosdeprogramacion.com?year=2023"))
print(FindParameters("https://retosdeprogramacion.com?year=2023&"))
print(FindParameters("https://retosdeprogramacion.com?year=&"))
print(FindParameters(
    "https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python"))
