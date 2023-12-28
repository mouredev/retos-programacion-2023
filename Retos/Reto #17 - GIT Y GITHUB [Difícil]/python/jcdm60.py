# Reto #17: Git y GitHub
#### Dificultad: Difícil | Publicación: 24/04/23 | Corrección: 01/05/23

## Enunciado

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

import requests

class GitHubAPI:
    def __init__(self, repo):
        self.repo = repo
        self.base_url = f"https://api.github.com/repos/{self.repo}"

    def get_commits(self, per_page=10):
        url = f"{self.base_url}/commits"
        params = {'per_page': per_page }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            commits = response.json()
            return commits
        else:
            print(f"Error al obtener los commits: {response.status_code}")
            return None

    def print_commits(self, per_page=10):
        commits = self.get_commits(per_page)
        if commits is not None:
            for commit in commits:
                sha = commit['sha']
                author = commit['commit']['author']['name']
                message = commit['commit']['message']
                date = commit['commit']['committer']['date']
                print(f"{sha}: {author}: {message} ({date})")


if __name__ == "__main__":
    url = "mouredev/retos-programacion-2023"
    github_api = GitHubAPI(url)
    github_api.print_commits()
