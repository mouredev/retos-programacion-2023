"""
/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
 */
"""
import requests
from bs4 import BeautifulSoup

url = "https://holamundo.day"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("blockquote", class_="BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width")

dates = []

for result in results:
    dates.append(result.text)


print(">_Agenda 8 de mayo | “Hola Mundo” day")

for activity in dates[19:]:
    print(activity)
    