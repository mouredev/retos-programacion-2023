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
 */
"""

import requests
from bs4 import BeautifulSoup

def Titulo(tag):
    return tag.name=="h1" and "Agenda 8 de mayo" in tag.text

def Agenda(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    Fecha = soup.find(Titulo)
    Horario = Fecha.find_all_next("blockquote", {"class": "BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width"})
    for Hora in Horario:
        print(Hora.get_text()) 
        
url="https://holamundo.day/"
Agenda(url)