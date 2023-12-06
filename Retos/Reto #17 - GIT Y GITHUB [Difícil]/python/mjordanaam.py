"""
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
import requests
import json

def get_date(datetime: str) -> str:
    year = datetime[:4]
    month = datetime[5:7]
    day = datetime[8:10]
    time = datetime[11:16]

    return day + "/" + month + "/" + year + " " + time


def read_last_10_commits(repo: str) -> None:
    url = f'https://api.github.com/repos/mouredev/{repo}/commits'
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    page = requests.get(url, headers)
    commits = json.loads(page.text)

    for i in range(0, 10):
        hash = commits[i]["sha"]
        author = commits[i]["commit"]["author"]["name"]
        message = commits[i]["commit"]["message"]
        datetime = get_date(commits[i]["commit"]["author"]["date"])

        print(f"Commit {i + 1} | {hash} | {author} | {message} | {datetime}")


read_last_10_commits("retos-programacion-2023")