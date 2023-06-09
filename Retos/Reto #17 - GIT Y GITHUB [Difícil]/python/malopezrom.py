# /*
# * ¡Estoy de celebración! He publicado mi primer libro:
#  * "Git y GitHub desde cero"
#  * - Papel: mouredev.com/libro-git
#  * - eBook: mouredev.com/ebook-git
#  *
#  * ¿Sabías que puedes leer información de Git y GitHub desde la gran
#  * mayoría de lenguajes de programación?
#  *
#  * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
#  * - Hash
#  * - Autor
#  * - Mensaje
#  * - Fecha y hora
#  *
#  * Ejemplo de salida:
#  * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21: 00
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.
#  *
#  */

import requests
from datetime import datetime

## Clase que representa un repositorio de GitHub

class GitHub:
    GIT_HUB_URL = 'https://api.github.com/repos/'

    def __init__(self, repository_name):
        self.repository_name = repository_name

    ##
    # Método que devuelve los últimos commits de un repositorio
    # @param commits número de commits a devolver
    # @return lista de commits

    def get_commits(self,commits):
        url = f"{self.GIT_HUB_URL}{self.repository_name}/commits?per_page={commits}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()

    ##
    # Método que imprime los commits
    # @param commits lista de commits

    def print_commits(self, commits):
        for index,commit in enumerate(commits):
            hash = commit['sha']
            author = commit['commit']['author']['name']
            message = commit['commit']['message']
            date = commit['commit']['author']['date']
            format_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")

            print(f"Commit {index} | {hash} | {author} | {message} | {format_date}")


## Método principal
if __name__ == '__main__':
    repository_name = 'mouredev/retos-programacion-2023'
    github = GitHub(repository_name)
    commits = github.get_commits(10)
    github.print_commits(commits)

