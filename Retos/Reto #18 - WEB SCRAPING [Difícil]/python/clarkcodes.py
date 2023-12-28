# Retos Semanales ‘23
# Reto #18: Web Scraping
# DIFÍCIL | Publicación: 01/05/23 | Resolución: 11/05/23
#
# El día 128 del año celebramos en la comunidad el "Hola Mundo day"
# Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
#
# Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
# del día 8. Mostrando hora e información de cada uno.
# Ejemplo: "16:00 | Bienvenida"
#
# Se permite utilizar librerías que nos faciliten esta tarea.

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 13/05/2023

# Imports
from bs4 import BeautifulSoup
import requests
import typer
from rich import print
from rich.table import Table

# Atributos Globales
URL = "https://holamundo.day" # URL de la cual se requiere consultar

# Funciones
def scraper():
    global URL
    title = ""

    response = requests.get( URL ).content  #Se obtiene el contenido de la página Web
    bs = BeautifulSoup( response, features="html.parser" )  #Se crea un objeto de BeautifulSoup con el contenido de la página web
    titles = bs.find_all( "h1", "StyledElement___StyledDiv-sc-2e063k-0 notion-h notion-h1 unset-width" )  #Se buscan todos los elementos que coincidan con estos parámetros
    blockquotes = bs.find_all( "blockquote" )

    for t in titles:  #Se busca el elemento de los titulos que coincida con este criterio y se lo asigna a la variable 'title'
        if( str( t.text ).find( ">_ Agenda 8" ) != -1 ):
            title = t.text
            break

    print( f"[bold yellow]\n{title}\n" )
    scheduleTable = Table( "Hora", "Descripción: Tema | Ponente" )  #Se crea una tabla con las cabeceras correspondientes para ver los datos ordenadamente
    
    for bq in blockquotes[21:]:  #Se recorren las blockquotes haciendo tratamiento de cadenas, detectando el separador para distribuir la información correctamente y quitarlo al final
        bqText = str( bq.text )
        separatorIndex = bqText.find(" | ")
        scheduleTable.add_row( bqText[0:separatorIndex],  bqText[separatorIndex + 3:] )  #Se añade una nueva fila por cada horario

    print( scheduleTable )


def main():
    print( "[bold green]\n*** Reto #18: WEB SCRAPING - By @ClarkCodes ***" )
    print( "[bold green]Web Scraping with Python" )

    scraper()

    print( "[green]\nEsto ha sido todo por hoy.\nMuchas gracias por ejecutar este Script, hasta la próxima... Happy Coding!, bye :D\nClark." )

# Llamada a la Función Principal
if __name__ == "__main__":
    typer.run( main )
