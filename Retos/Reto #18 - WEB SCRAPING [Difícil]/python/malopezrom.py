# /*
# * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
# * Vamos a hacer "web scraping" sobre su sitio web: https: // holamundo.day
# *
# * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
# * del día 8. Mostrando hora e información de cada uno.
# * Ejemplo: "16:00 | Bienvenida"
# *
# * Se permite utilizar librerías que nos faciliten esta tarea.
# *
# */



import requests
from bs4 import BeautifulSoup




def print_day_8():
    url = "https://holamundo.day"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("h1")

    for result in results:
        if(result.text.find("Agenda 8 de mayo") != -1):
            print(result.text)
            sibling = result.next_siblings
            for agenda in sibling:
                if(agenda.name == "blockquote"):
                    print(agenda.text)


print_day_8()

