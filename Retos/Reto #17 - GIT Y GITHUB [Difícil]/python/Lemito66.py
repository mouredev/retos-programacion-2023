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

import requests

def show_date(date: str) -> str:
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    time = date[11:16]

    return day + "/" + month + "/" + year + " " + time


def get_repository(username: str, name: str, number_of_commits: int):
    try:
        url = f'https://api.github.com/repos/{username}/{name}/commits'
        response = requests.get(url)
        json_response = response.json()

        for i in range(number_of_commits):
            print(
                f'Commit {i+1} | {json_response[i]["sha"]} | {json_response[i]["commit"]["author"]["name"]} | {json_response[i]["commit"]["message"]} | {show_date(json_response[i]["commit"]["author"]["date"])}')
    except:
        print('An exception occurred')


get_repository('lemito66', 'django-crud-react',10)
