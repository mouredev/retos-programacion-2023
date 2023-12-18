"""
Vamos a asumir lo siguiente:
- La fuente de información será el árbol de directorios de un repositorio descargado en local.
- Seleccionamos los problemas afectados usando la fecha de 'Publicación' en su fichero 'ejercicio.md'.
- Para cada fichero xyz.ext asumiremos que el autor es 'xyz'. La presencia de un fichero xyz.ext dentro
  de una carpeta 'Reto #xx - <desc> [dif]/<lang>/' supondrá asumir que el usuario 'xyz' resolvió el
  Reto número 'xx'.
- Si un usuario ha resuelto un Reto en más de un lenguaje de programación, se contará como una única
  resolución, no varias.
"""
from datetime import datetime
from pathlib import Path
import re
import sys


DEFAULT_DIR = Path(__file__).parent.parent.parent
CURRENT_YEAR = 2023


def main():
    base_dir = DEFAULT_DIR
    if len(sys.argv) > 1:
        base_dir = Path(sys.argv[1])

    challenge_dir_list = get_challenge_dir_list(base_dir, year=CURRENT_YEAR)

    if not challenge_dir_list:
        msg = (
            f"Error while using '{base_dir}' as base directory.\n"
            "Hint: you can pass the base folder as the first argument to the script.\n"
            "The base dir is expected to be the folder containing the 'Reto #xx - ...' folders."
        )
        print(msg)
        return

    user_data = {}
    for challenge_dir in challenge_dir_list:
        solvers = get_solver_users(challenge_dir)
        for solver in solvers:
            user_data[solver] = user_data.get(solver, 0) + 1

    dsu = [(v, k) for k, v in user_data.items()]

    for n_solved, user_name in sorted(dsu, reverse=True):
        print(f"{n_solved:2d} {user_name}")

    n_users, n_solutions = count_users_and_solutions_from(user_data)

    print(f"Total users: {n_users}\nTotal solutions sent: {n_solutions}")


def get_challenge_dir_list(folder: Path, year: int | None) -> list[Path] | None:
    """
    Given a dir 'folder', return all the 'Reto #xx - ...' folders inside it.
    If not possible, return None.

    Args:
        folder (Path):
            Folder inside which we want to search.
        year (int):
            Return results only for this year. If not given, do not filter by year.

    Returns:
        List of Paths, where each Path is a 'Reto #xx - ...' folder. If we can not get
        the list (e.g., 'folder' is not a directory), return None.
    """
    if not folder.is_dir():
        return None

    patt = re.compile(r"Reto #\d+ - .+ \[.+]")

    dir_list = [d for d in folder.iterdir() if patt.match(d.name)]

    if year is not None:
        dir_list = [d for d in dir_list if challenge_belongs_to_year(d, year)]

    return dir_list


def get_solver_users(challenge_dir: Path) -> set:
    """
    Given a challenge dir 'challenge_dir', return a list of all users that
    solved this challenge.

    Args:
        challenge_dir (Path):
            Challenge directory where we will search for all users that solved it.

    Returns:
        Set containing the usernames of all users having solved the challenge.
    """
    solvers = set()

    for lang_dir in challenge_dir.iterdir():
        if not lang_dir.is_dir():
            continue

        for script in lang_dir.iterdir():
            user_name = script.name.split(".")[0]
            solvers.add(user_name)

    return solvers


def count_users_and_solutions_from(user_data: dict) -> tuple[int, int]:
    """
    Given a dictionary with user data as {user_name: number of problems solved},
    return the total amount of users, and the total amount of solutions sent.
    """
    return len(user_data), sum(user_data.values())


def challenge_belongs_to_year(folder: Path, year: int) -> bool:
    """
    Given a challenge dir 'folder', and a year 'year', return True if the directory
    corresponds to a challenge issued in the year 'year'. We decide that by looking
    at the ejercicio.md file. If no 'ejercicio.md' file exists, we assume a negative.

    Args:
        folder (Path):
            Challenge folder that we know to identify as belonging to a given year, or not.
        year (int):
            Year to which we want to know whether the challenge belongs or not.

    Returns:
        True if the challenge in 'folder' was issued in year 'year'. False, otherwise.
    """
    patt = re.compile(r"(?<=Publicación: )[\d/]+")
    for markdown_file in folder.glob("ejercicio.md"):  # only one or zero matches, because we give the exact file name
        with open(markdown_file, "r") as f:
            for line in f:
                m = patt.search(line)
                if m:
                    try:
                        challenge_date = datetime.strptime(m.group(0), "%d/%m/%y")
                    except ValueError:
                        return False

                    return challenge_date.year == year

    return False


if __name__ == "__main__":
    main()
