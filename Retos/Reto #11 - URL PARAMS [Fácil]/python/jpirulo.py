class URL:
    def __init__(self, url):
        self.url = url

    def obtener_valores_de_parametros(self):
        partes_url = self.url.split("?") #divido el url
        if len(partes_url) < 2:
            raise ValueError("La URL no contiene una cadena de consulta")

        query_string = partes_url[1] #si tiene 2 partes obtengo la  segunda 

        parametros = query_string.split("&") #obtengo los parametos en una lista
        valores = []
        for parametro in parametros:
            partes_parametro = parametro.split("=")
            if len(partes_parametro) < 2:
                raise ValueError("El parámetro no tiene un valor")
            valor = partes_parametro[1]
            valores.append(valor)

        return valores


mi_url = URL(
    "http://example.com?product=1234&utm_source=google&edad=50&pais=Venezuela")
valores = mi_url.obtener_valores_de_parametros()
print(valores) 
