"""
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
"""

import requests


def commit_list():
    url = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits"
    res = requests.get(url)
    data = res.json()
    commit_list = ''

    for i in range(10):
        commit_list += "* Commit {} | {} | {} | {} | {}\n".format(
            i + 1, data[i]['sha'][:7], data[i]['commit']['author']['name'], data[i]['commit']['message'].replace('\n', ' '), data[i]['commit']['author']['date'])

    print(commit_list)


commit_list()
