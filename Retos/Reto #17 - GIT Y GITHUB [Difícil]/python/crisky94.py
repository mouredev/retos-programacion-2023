# /*
#  * ¡Estoy de celebración! He publicado mi primer libro:
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
#  * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.
#  * 
#  */

import requests

def last_commit(num_commits= 10):
    url = 'https://api.github.com/repos/mouredev/retos-programacion-2023/commits'
    params = {'per_page': num_commits}

    response = requests.get(url, params= params)

    if response.status_code != 200:
        print(f"Error al obtener los datos: {response.status_code}")
        return[]

    commits = response.json()
    commit_data = [];

    for commit in commits:
        commit_info={
            'hash' : commit['sha'],
            'autor' : commit['commit']['author']['name'],
            'message' : commit['commit']['message'],
            'date_time' : commit['commit']['author']['date']
        }

        commit_data.append(commit_info)
    return commit_data

def print_commits(commits):
    for index, commit in enumerate(commits, start=1):
        print(f"Commit #{index}")
        print(f" - Hash: {commit['hash']}")
        print(f" - Mensaje: {commit['message']}")
        print(f" - Fecha y hora: {commit['date_time']}")
        print('-' * 40)

commits = last_commit(10)

if commits:
    print_commits(commits)