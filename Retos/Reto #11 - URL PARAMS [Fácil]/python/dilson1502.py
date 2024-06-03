def obtener_parametros_url(url:str)->list:
    """This function returns the params of a given url

    Args:
        url (str): 

    Returns:
        list: url params
    """

    query = url.split("?")
    if len(query)<=1:
        return []
    parametros = query[1].split("&")
    valor_parametros = []
    for parametros in parametros:
        valor_parametros.append(parametros.split("=")[1])
    return valor_parametros

# Ejemplo: En la 
#  * los parámetros serían ["2023", "0"]

if __name__=="__main__":
    url = "https://retosdeprogramacion.com?year=2023&challenge=0&test=true"
    parametros = obtener_parametros_url(url)
    print(parametros)
