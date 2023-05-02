# Retos Semanales ‘23
# Reto #17: GIT Y GITHUB
# DIFÍCIL | Publicación: 24/04/23 | Resolución: 01/05/23
#
# ¡Estoy de celebración! He publicado mi primer libro:
# "Git y GitHub desde cero"
# - Papel: mouredev.com/libro-git
# - eBook: mouredev.com/ebook-git
#
# ¿Sabías que puedes leer información de Git y GitHub desde la gran
# mayoría de lenguajes de programación?
#
# Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
# - Hash
# - Autor
# - Mensaje
# - Fecha y hora
#
# Ejemplo de salida:
# Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
#
# Se permite utilizar librerías que nos faciliten esta tarea.
# 

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 25/04/2023

# Imports
import requests
from datetime import datetime

# Atributos Globales
# Constants - Establecer estos parámetros configurables
GH_AUTH_TOKEN = "YOUR_ACCESS_TOKEN" # Reemplaza la cadena YOUR_ACCESS_TOKEN por tu Token de Acceso Personal de GitHub
REPOSITORY = "mouredev/retos-programacion-2023"
COMMITS_CANT = "10"

# Funciones
def gitHubCommitsReader():
    # Se preparan los parámetros para realizar la petición GET contra la API de GitHub
    url = "https://api.github.com/repos/" + REPOSITORY + "/commits?per_page=" + COMMITS_CANT
    headers = { "Authorization" : "token " + GH_AUTH_TOKEN }
    
    try:
        response = requests.get( url, headers=headers ) # Se ejecuta la petición y se obtienen los resultados
        commits = response.json()
    
        print( f"Estos son los últimos { COMMITS_CANT } Commits(el más reciente primero) del Repositorio '{ REPOSITORY }':" )
    
        for i, commit in enumerate( commits ):
            # Se da formato a Información obtenida que lo necesite
            msj = str( commit['commit']['message'] ).replace( "\n", "." ).replace( "..", " | " ) # Se reemplazan saltos de línea del Mensaje si los tuviera por un caracter de separación con espacios (' | '), usualmente son dos saltos de línea
            fechaHora = datetime.strptime( str( commit['commit']['committer']['date'] ), "%Y-%m-%dT%H:%M:%SZ" ).strftime( "%d/%m/%Y - %H:%M" ) # Se aplica Formato de Fecha y hora user friendly
        
            print( f"\n** Commit #{ i + 1 } **" )
            print( f"\tHash: { commit['sha'] }" )
            print( f"\tAutor: { commit['commit']['author']['name'] }" )
            print( f"\tMensaje: { msj }" )
            print( f"\tFecha y Hora: { fechaHora }" )

    except:
        print( "Oops... algo no ha salido bien, verifique por favor." )

def main():
    print( "\n*** Reto #17: GIT Y GITHUB - By @ClarkCodes ***" )
    print( "* Obteniendo Commits * - Un momento por favor..." )

    gitHubCommitsReader()

    print( "\nEsto ha sido todo por hoy.\nMuchas gracias por ejecutar este Script, hasta la próxima... Happy Coding!, bye :D\nClark." )

# Llamada a la Función Principal
main()

