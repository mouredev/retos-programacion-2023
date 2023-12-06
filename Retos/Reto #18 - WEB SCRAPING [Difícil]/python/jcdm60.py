#
# El día 128 del año celebramos en la comunidad el "Hola Mundo day"
# Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
#
# Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
# del día 8. Mostrando hora e información de cada uno.
# Ejemplo: "16:00 | Bienvenida"
#
# Se permite utilizar librerías que nos faciliten esta tarea.
#

from bs4 import BeautifulSoup
import requests

class HolaMundoDay:
    def __init__(self, url):
        self.url = url

    def get_page_content(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')

    def get_day(self):
        soup = self.get_page_content()
        day = soup.find_all('h1')[-2]
        return day.text if day else None

    def get_quotes(self):
        soup = self.get_page_content()
        for quote in soup.find_all("blockquote")[-15:]:
            print(quote.text)
        

url = "https://holamundo.day/"
hm = HolaMundoDay(url)
print(hm.get_day())
hm.get_quotes()

