# Reto #17: Git y GitHub
#### Dificultad: Difícil | Publicación: 24/04/23 | Corrección: 01/05/23
## Enunciado
#
# ¡Estoy de celebración! He publicado mi primer libro:
# "Git y GitHub desde cero"
# - Papel: mouredev.com/libro-git
# - eBook: mouredev.com/ebook-git
#
# ¿Sabías que puedes leer información de Git y GitHub desde la gran
# mayoría de lenguajes de programación?
#
# Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
# - Hash
# - Autor
# - Mensaje
# - Fecha y hora
#
# Ejemplo de salida:
# Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
#
# Se permite utilizar librerías que nos faciliten esta tarea.
# 
import requests


from typing import Generator


def get_repo_commits(repo: str) -> str:
    return f"https://api.github.com/repos/{repo}/commits"


def all_commits(repo_url: str) -> list[dict]:
    try:
        return requests.get(repo_url).json()
    except requests.exceptions.RequestException as err:
        print(err)


def format_commits(commits: list[dict]) -> Generator:
    return (f"commit #{str(i+1)} | hash={str(commit['sha'])} | Author={commit['commit']['author']['name']} | Message={commit['commit']['message']} | Date={commit['commit']['author']['date']}" for i, commit in enumerate(commits))


def commits_to_show(number: int = 10) -> int:
    try:
        return abs(int(number))
    except ValueError:
        print(ValueError(
            f"Invalid value for 'number': '{number}'. Please enter a valid integer."))


def generate_commits(commits: Generator, number: int = 10, mode="DESC") -> list[str]:
    mode = mode.upper()
    commit_mode: tuple[str, str] = ("ASC", "DESC")

    try:
        if mode not in commit_mode:
            raise ValueError(f"PLace a valide mode: {commit_mode}")
    except ValueError as err:
        print(err)

    if mode == commit_mode[0]:
        return [commit for commit in commits][:number]

    return [commit for commit in commits][-number:]


def main() -> None:
    repo_to_use = get_repo_commits(repo="mouredev/retos-programacion-2023")
    available_commits = all_commits(repo_url=repo_to_use)
    formatted_commits = format_commits(commits=available_commits)
    commits_number_to_show = commits_to_show(number="5")

    commits = generate_commits(
        formatted_commits, commits_number_to_show, mode="asc")
    print(commits)


if __name__ == "__main__":
    main()