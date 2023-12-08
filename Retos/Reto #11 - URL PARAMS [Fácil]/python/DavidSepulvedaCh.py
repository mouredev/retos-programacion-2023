def obtener_valores_parametros(url):
    partes = url.split('?')
    if len(partes) == 2:
        parametros = partes[1]
        parametros_lista = parametros.split('&')
        valores_parametros = []
        for parametro in parametros_lista:
            clave_valor = parametro.split('=')
            if len(clave_valor) == 2:
                valores_parametros.append(clave_valor[1])
        
        return valores_parametros
    return []

url = "https://retosdeprogramacion.com?year=2023&challenge=0"
valores_parametros = obtener_valores_parametros(url)
print(valores_parametros)
