# Reto #17: Git y GitHub
"""/*
 * ¡Estoy de celebración! He publicado mi primer libro:
 * "Git y GitHub desde cero"
 * - Papel: mouredev.com/libro-git
 * - eBook: mouredev.com/ebook-git
 *
 * ¿Sabías que puedes leer información de Git y GitHub desde la gran
 * mayoría de lenguajes de programación?
 *
 * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
 * - Hash
 * - Autor
 * - Mensaje
 * - Fecha y hora
 *
 * Ejemplo de salida:
 * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 * 
 */"""

from git import Repo
import time

repo_url = "https://github.com/mouredev/retos-programacion-2023"

repo = Repo("/users/jmiguelmangas/git_prueba")

tree = repo.head.commit.tree

prev_commits = [
    c for c in repo.iter_commits(all=True, max_count=10)
]  # last 10 commits from all branches

i = 1
for commit in prev_commits:
    hora1 = time.asctime(time.gmtime(commit.committed_date))
    hora2 = time.strftime("%a, %d %b %Y %H:%M", time.gmtime(commit.committed_date))
    print(
        f"Numero de Commit {i} Hash: {commit} \nAutor {commit.author.name} \nMensaje: {commit.message} \nFecha: {hora1}\n\n"
    )
    i += 1
