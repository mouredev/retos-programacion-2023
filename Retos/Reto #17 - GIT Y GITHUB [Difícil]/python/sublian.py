# Reto #17: Git y GitHub
#### Dificultad: Difícil | Publicación: 24/04/23 | Mi solución: 24/10/23
## Enunciado
"""
 * ¡Estoy de celebración! He publicado mi primer libro:
 * "Git y GitHub desde cero"
 * - Papel: mouredev.com/libro-git
 * - eBook: mouredev.com/ebook-git 
 * ¿Sabías que puedes leer información de Git y GitHub desde la gran
 * mayoría de lenguajes de programación?
 * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
 * - Hash
 * - Autor
 * - Mensaje
 * - Fecha y hora
 * Ejemplo de salida:
 * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
 * Se permite utilizar librerías que nos faciliten esta tarea.
""" 

import requests

class GithubService:
    def __init__(self, repo):
        self.repo = repo
        self.base_url = f" https://api.github.com/repos/{self.repo}"
        
    def get_commits(self, per_page=10):
        url= f"{self.base_url}/commits"
        params = {"per_page": per_page}
        #manejo de errores
        try:            
            response = requests.get(url, params = params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error) from None
        return response.json()
    
    def print_commits(self):
        commits = self.get_commits()
        if not commits:
            return None
        for index, commit in enumerate(commits):
            #Disminuyo el tamaño de SHA
            sha= commit.get("sha")[:7]
            _commit = commit.get("commit")
            author = _commit.get("author").get("name")
            #Con el replace elimino el salto de linea que viene con message
            message = _commit.get("message").strip().replace('\n','')
            #Disminuyo el tamaño de fecha a YY-MM-DD
            date = _commit.get("committer").get("date")[:10]
            #Muestro el mensaje solicitado
            print(f"Commit: {index+1}. {sha} | {author} | {message} | {date}")
                
            
        
if __name__ == "__main__":
    url= "mouredev/retos-programacion-2023"
    github_service = GithubService(url)
    github_service.print_commits()
    