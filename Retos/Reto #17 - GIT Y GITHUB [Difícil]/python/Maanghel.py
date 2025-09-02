"""
¡Estoy de celebración! He publicado mi primer libro:
"Git y GitHub desde cero"
- Papel: mouredev.com/libro-git
- eBook: mouredev.com/ebook-git

¿Sabías que puedes leer información de Git y GitHub desde la gran
mayoría de lenguajes de programación?

Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
- Hash
- Autor
- Mensaje
- Fecha y hora

Ejemplo de salida:
Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00

Se permite utilizar librerías que nos faciliten esta tarea.
"""

import git

def print_commits(cantity: int = 10, repo_path: str = ".") -> None:
    """
    Print the most recent commits from a Git repository.

    This function retrieves and displays commit information such as
    hash, author, message, and date for a specified number of commits.

    Args:
        cantity (int): Number of commits to display (default: 10).
        repo_path (str): Path to the Git repository (default: current directory).

    Raises:
        FileNotFoundError: If the provided directory does not exist.
        RuntimeError: If the provided directory is not a valid Git repository.

    Returns:
        None: The function only prints output to the console.
    """
    try:
        repo = git.Repo(repo_path)
    except git.exc.NoSuchPathError as e:
        raise FileNotFoundError("El directorio no existe.") from e
    except git.exc.InvalidGitRepositoryError as e:
        raise RuntimeError("El directorio no es un repositorio Git válido.") from e

    for index, commit in enumerate(list(repo.iter_commits())[:cantity], 1):
        date = commit.committed_datetime.strftime("%d/%m/%Y %H:%M")
        print("—" * 60)
        print(f"Commit: {index}")
        print(f"Hash: {commit.hexsha}")
        print(f"Author: {commit.author}")
        print(f"Message: {commit.message}".replace("\n", ""))
        print(f"Date: {date}")


if __name__ == "__main__":
    print_commits()
