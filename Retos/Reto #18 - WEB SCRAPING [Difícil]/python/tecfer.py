'''
El día 128 del año celebramos en la comunidad el "Hola Mundo day"
Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day

Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
del día 8. Mostrando hora e información de cada uno.
Ejemplo: "16:00 | Bienvenida"

Se permite utilizar librerías que nos faciliten esta tarea.
'''
#pip install beautifulsoup4
#pip install lxml

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://holamundo.day/').content, 'lxml')

elementos = soup.find_all('blockquote')
for elemento in elementos[21:]:
    print(elemento.get_text())
  
