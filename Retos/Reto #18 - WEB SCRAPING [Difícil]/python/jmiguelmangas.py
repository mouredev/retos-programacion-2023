"""/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
 */"""
import requests
import csv
from bs4 import BeautifulSoup


def indextoentry(lista, index):
    listresult = []
    listresult = listresult.append(lista[index])
    return listresult


url = "https://holamundo.day/"
response = requests.get(url)

html = BeautifulSoup(response.text, "html.parser")

quotes_html = html.find_all(
    "blockquote",
    class_="notion-quote",
)

quotes = list()

for quote in quotes_html:
    quotes.append(quote.text)
quotes_filtered = list()
for quote in quotes:
    if ":" in quote:
        quotes_filtered.append(quote)

for i in range(7, len(quotes_filtered)):
    print(quotes_filtered[i])
