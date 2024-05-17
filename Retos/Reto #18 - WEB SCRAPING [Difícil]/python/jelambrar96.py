#!/usr/bin/python3

"""
# Reto #18: Web scraping
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
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


from bs4 import BeautifulSoup
import requests


URL = "https://holamundo.day/"


def main():
    web = requests.get(URL)
    agenda = {}

    soup = BeautifulSoup(web.content, 'html.parser')

    results = soup.find_all('blockquote')
    dates = [ item.text for item in results ]

    for act in dates[13:]:
        print(act)



if __name__ == '__main__':
    main()
