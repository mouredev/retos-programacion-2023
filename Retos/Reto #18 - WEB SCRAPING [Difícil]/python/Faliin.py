import requests
from bs4 import BeautifulSoup

# Realizar la solicitud HTTP a la página web
url = "https://holamundo.day"
response = requests.get(url)

# Crear el objeto BeautifulSoup para analizar el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la sección de la agenda del día 8
agenda = soup.find("div", {"class": "Agenda 8 de mayo"})
events = agenda.find_all("div", {"class": "event"})

# Imprimir la hora e información de cada evento del día 8
for event in events:
    time = event.find("span", {"class": "time"}).text.strip()
    info = event.find("span", {"class": "info"}).text.strip()
    print(f"{time} | {info}")
