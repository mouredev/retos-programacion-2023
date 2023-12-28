'''/*
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
 */'''

import git

ruta_repositorio = 'retos_mourodev\\retos-programacion-2023'
repo = git.Repo(ruta_repositorio)
commits = list(repo.iter_commits())[:10][::-1]
for idx, commit in enumerate(commits, 1):
    mensaje = commit.message.splitlines()[0] 
    print(f'Commit {idx}| {commit.hexsha} | {commit.author.name} | {mensaje} | {commit.authored_datetime}')

