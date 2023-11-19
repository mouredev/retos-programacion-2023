from urllib.parse import urlparse, parse_qs

def obtener_valores_parametros(url):
    # Obtener la parte de la consulta de la URL
    parsed_url = urlparse(url)
    
    # Obtener un diccionario con los valores de los parámetros
    parametros_dict = parse_qs(parsed_url.query)

    # Convertir el diccionario a un diccionario de claves y valores
    clave_valor_dict = {clave: valor[0] for clave, valor in parametros_dict.items()}
    
    return clave_valor_dict

url_ejemplo = "https://retosdeprogramacion.com?year=2023&challenge=0"
resultado = obtener_valores_parametros(url_ejemplo)
for clave, valor in resultado.items():
    print(clave,':', valor)
