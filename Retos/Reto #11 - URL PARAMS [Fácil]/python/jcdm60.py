#
# Dada una URL con parámetros, crea una función que obtenga sus valores.
# No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#
# Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
# los parámetros serían ["2023", "0"]
#


def obtener_parametros(url):
    signo = url.find("?")
    if signo == -1:
        return []

    # Si hay signo "?", obtenemos la cadena de parámetros
    parametros = url[signo + 1 :]

    # Dividimos la cadena de parámetros en pares "clave=valor"
    pares_valor = parametros.split("&")

    # Para cada par "clave=valor", obtenemos el valor y lo agregamos a una lista
    valores = []
    for par in pares_valor:
        par_lista = par.split("=")
        if len(par_lista) >= 2 and par_lista[1]:
            valor = par_lista[1]
            valores.append(valor)

    return valores

if __name__ == "__main__":
    url1 = "https://retosdeprogramacion.com?year=2023&challenge=0"
    url2 = "https://retosdeprogramacion.com/search?year=2023"
    url3 = "https://retosdeprogramacion.com/params/name/lastname"
    url4 = "retosdeprogramacion.com/search?"
    url5 = ""

    print(obtener_parametros(url1))
    print(obtener_parametros(url2))
    print(obtener_parametros(url3))
    print(obtener_parametros(url4))
    print(obtener_parametros(url4))