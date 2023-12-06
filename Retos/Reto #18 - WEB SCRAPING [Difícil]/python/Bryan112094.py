# El día 128 del año celebramos en la comunidad el "Hola Mundo day"
# Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day

# Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
# del día 8. Mostrando hora e información de cada uno.
# Ejemplo: "16:00 | Bienvenida"

# Se permite utilizar librerías que nos faciliten esta tarea.
from bs4 import BeautifulSoup
import requests

class Horarios:
    def __init__(self, url):
        self.url = url

    #Comprobar si la url funciona
    def url_go(self):
        try:
            link = requests.get(self.url)
            link.raise_for_status()
            return link.content
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        
    #Obtener el listado del horario del holamundoday
    def listado_horario(self, soup) -> list:
        #busca el h1 que tenga el texto: Agenda 8 de mayo
        busca = soup.find_all(string=" Agenda 8 de mayo | ")[0].find_parent("h1")
        lista = []
        for s in busca.find_all_next("blockquote"):
            lista.append(s.get_text())
        return lista
    
    #imprimir todos los horarios
    def print_horarios(self, horarios):
        print('Agenda 8 de mayo | “Hola Mundo” day')
        for horario in horarios:
            print(horario)
        
    def start(self):
        content = self.url_go()
        soup = BeautifulSoup(content, 'html.parser')
        horarios = self.listado_horario(soup)
        self.print_horarios(horarios)

HolaMundoDay = Horarios('https://holamundo.day/')
HolaMundoDay.start()