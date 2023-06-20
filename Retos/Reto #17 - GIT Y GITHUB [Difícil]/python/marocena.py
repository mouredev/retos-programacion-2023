'''
/*
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
 */
'''

from github import Github

def get_hash(commit) -> str:

    return commit.sha[:6]

def get_author(commit) -> str:

    return commit.commit.author.name

def get_comment(commit) -> str:

    return commit.commit.message

def get_date(commit) -> str:

    return commit.commit.author.date.strftime("%d/%m/%Y %H:%M")


g = Github("access_token")

repo = g.get_repo("mouredev/retos-programacion-2023")

for i, commit in enumerate(repo.get_commits()[:10]):

    hash = get_hash(commit)
    author = get_author(commit)
    message = get_comment(commit)
    date = get_date(commit)


    print(f"* Commit {i+1} | {hash} | {author} | {message} | {date}\n")
