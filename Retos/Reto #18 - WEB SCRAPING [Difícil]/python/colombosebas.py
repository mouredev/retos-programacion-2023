import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Bueno es un poco rebuscado pero salió, basicamente lo que hago es obtener todo el html de la web y luego lo analizo con el ElementTree
# lo que hago es ir viendo como estan formados los textos del xml y en base a eso veo que muestro y que no. Cualquier cambio en la web
# podría llegar a romper el correcto funcionamiento de este algoritmo.
# Seguramente alguno encontró una manera más simple de hacerlo :)

url = 'https://holamundo.day'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
html_str = soup.prettify()
root = ET.fromstring(html_str)
agenda8 = False
cadena = ""

for elem in root.iter():
    texto = str(elem.text)
    if agenda8 == False:
        if ((texto.find("Agenda 8 de mayo") != -1) and (elem.tag == 'span')):
            agenda8 = True
            print("Agenda 8 de Mayo")
        atributo = str(elem.attrib)
    elif(elem.tag == 'span') and (atributo.find("data-slate-string") != -1):
        texto2 = str(elem.text)
        texto2 = texto2.replace(" ", "")
        texto2 = texto2.strip()
        if len(texto2) >= 1:
            if texto2.startswith("1") or texto2.startswith("2"):
                print(cadena)
                cadena = texto2
            else:
                if texto2 == '|':
                    cadena += " " + texto2
                else:
                    cadena += texto2
           #print(f'Texto:{texto2.strip()}*')
        if texto2.find("Despedida") != -1:
            break
