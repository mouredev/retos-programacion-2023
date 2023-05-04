'''
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
'''

import requests
from bs4 import BeautifulSoup

url = 'https://holamundo.day'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for quote in soup.find_all("blockquote")[-15:]:

    print(quote.text)