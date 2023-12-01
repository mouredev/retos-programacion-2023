# Reto #18: Web scraping
#### Dificultad: Difícil | Publicación: 01/05/23 | Mi Solucion: 30/10/23
## Enunciado
"""
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 * Se permite utilizar librerías que nos faciliten esta tarea.
 
 El sitio web https://holamundo.day no esta disponible por eso hare un web scraping a otra 
 pagina web, tomare como ejemplo la del equipo de futbol peruano solo como practica
 
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

#url a usar
url =('https://www.futbolperuano.com/liga-1/tabla-de-posiciones')
response = requests.get(url)

#si obtengo conexion 200 procedo con el codigo
if response.status_code ==200:
    soup = BeautifulSoup(response.content, 'html.parser')
    teams = soup.find_all('td', class_='equipo text-left')
    
    #para manipular la informacion creo una lista vacia
    selection = list()
    for team in teams:
        #para evitar saltos de linea o espacios en blanco uso strip() y text() para que no salga otra informacion
        selection.append(team.text.strip()) 
        
    #print(selection)        
    #print("tamaño: ",len(selection))
    #para conocer el tamaño use la funcion len
    data = pd.DataFrame({'Equipos: ':selection}, index=list(range(1,39) ))
    print(data)
    
    #como extra creo un csv
    data.to_csv('Equipos de futbol peruano')
else:
    print("Error, no se logro conectar")
