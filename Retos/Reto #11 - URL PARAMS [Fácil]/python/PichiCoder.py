from urllib.parse import urlparse

def valores_url(url: str) -> list:
    
    parametros = urlparse(url)[4].split("&")
    
    return [parametro.split("=")[1] for parametro in parametros]

#Prueba
print(valores_url("https://retosdeprogramacion.com?year=2023&challenge=0"))
