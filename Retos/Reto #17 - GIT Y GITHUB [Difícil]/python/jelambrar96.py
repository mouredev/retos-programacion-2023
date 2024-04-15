#!/usr/bin/python3

"""
# Reto #17: Git y GitHub
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
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


import requests


URL = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits"


def get_repository_data(repo_url):
    data = {}
    try:
        response = requests.get(repo_url)
        data = response.json()
    except:
        pass
    return data


def show_commit_data(commit_data, n=10):
    for i,item in enumerate(commit_data):
        sha = commit_data[i]['sha']
        author = commit_data[i]['commit']['author']['name']
        message = commit_data[i]['commit']['message'].replace('\n', ' ')
        datetime = commit_data[i]['commit']['author']['date']
        
        print("Commit {}".format(i+1))
        print("Sha: {}".format(sha))
        print("author: {}".format(author))
        print("message: {}".format(message))
        print("datetime: {}".format(datetime))
        print()
        
        if i >= n:
            break


if __name__ == '__main__':
    data = get_repository_data(URL)
    show_commit_data(data, n=10)




