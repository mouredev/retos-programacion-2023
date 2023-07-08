# ¡Estoy de celebración! He publicado mi primer libro:
# "Git y GitHub desde cero"
# - Papel: mouredev.com/libro-git
# - eBook: mouredev.com/ebook-git
# ¿Sabías que puedes leer información de Git y GitHub desde la gran
# mayoría de lenguajes de programación?
# Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
# - Hash
# - Autor
# - Mensaje
# - Fecha y hora
# Ejemplo de salida:
# Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
# Se permite utilizar librerías que nos faciliten esta tarea.

from git import Repo
import pathlib

def listCommits(numero):
    repositorio = Repo(pathlib.Path(__file__).parent.resolve(), search_parent_directories=True)
    commits = list(repositorio.iter_commits(repositorio.active_branch, max_count=numero))
    for i in range(numero):
        print(F"Commit {str(i + 1)}: {commits[i].hexsha}\n Autor: {commits[i].author.name}\n Mensaje: {commits[i].message.splitlines()[0]}\n Fecha y hora: {str(commits[i].committed_datetime)}\n")

listCommits(10)