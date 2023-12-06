
def obtener_params(url: str) -> list[str] | str:

    try:
        parametros = url.split("?")[1]
    except Exception as e:
        return "No hay parametros en la url"    

    parametros = parametros.split('&')  # Si no hay un & directamente envia el string a una lista
    list_params = []

    for param in parametros:
        try:
            list_params.append(param.split('=')[1])
        except Exception as e:
            # Si el codigo llega hasta aqui es porque no pudo separar con = y por lo tanto hubo indexerror
            continue
    
    if len(list_params) > 0:
        return list_params
    else:
        return "Error al obtener los parametros"


if __name__ == '__main__':
    print(obtener_params('https://retosdeprogramacion.com?year=2023&challenge=0'))
    print(obtener_params('sdfsdfjkhb'))
    print(obtener_params('url.com?parametro1sdfs&parametro2owusdb'))
    print(obtener_params('url.com?parametro1=dfsujbdg&parametro2=hola&parametro3=mundo'))
