#  * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
#  * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
#  *
#  * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
#  * del día 8. Mostrando hora e información de cada uno.
#  * Ejemplo: "16:00 | Bienvenida"
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.

import requests
from parsel import Selector

url = "https://holamundo.day"

response = requests.get(url)

sel = Selector(response.text)

agenda = sel.css("blockquote")[-15:]
for event in agenda:
    # Print each event to the console
    print("".join(event.css("span::text").getall()))

