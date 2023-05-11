import requests
from lxml import html

encabezados = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "https://holamundo.day/"

respuesta = requests.get(url, headers=encabezados) ### Pasamos la petición

parser= html.fromstring(respuesta.text) ### pasamos todo el contenido para parsearlo


texto_horario_8_mayo = parser.xpath("//blockquote[position()>7 and position()<23]/span[*]/span//text()") ### nos quedamos con la parte del 8 de mayo

### Vamos con un bucle a imprimir la información
i = 0

while i<len(texto_horario_8_mayo):
    if texto_horario_8_mayo[i][0]!="1" and texto_horario_8_mayo[i][0]!="2": ### imprimo normal (sin saltos de línea a no ser que empiece por 1 o por 2
        print(texto_horario_8_mayo[i],end="")
    else:
        print(f"\n{texto_horario_8_mayo[i]}", end="") ### imprimo un salto de línea previo si empieza por 1 o por 2
    i+=1
