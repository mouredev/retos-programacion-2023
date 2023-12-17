"""
 * Todo llega a su fin... Este es el último reto de programación 
 * semanal de 2023.
 *
 * Crea un programa que muestre un listado calculado en tiempo real
 * con todos los usuarios que han resuelto algún reto de programación
 * de este año.
 * - El listado debe estar ordenado por el número de ejercicios resueltos
 *   por cada usuario (y mostrar ese contador al lado de su nombre).
 * - También se debe de mostrar el número de usuarios que han participado
 *   y el número de correcciones enviadas.
 *
 * Muchísimas gracias por ayudar a crear este gran recurso
 * para la comunidad... ¡Prepárate para 2024!   
"""
import git
import os
from itertools import islice


def main():
    repo_URL = "https://github.com/mouredev/retos-programacion-2023"    
    repo_directory_name = "/home/icedrek/Escritorio/RetoMoure"
    base_path = "/home/icedrek/Escritorio/RetoMoure/Retos"

    recover_repository(repo_URL, repo_directory_name)

    ranking = get_ranking(base_path)

    position = 1
    
    # muestra 100 primeros resultados
    for user, counter in islice(ranking.items(), 100):  
        print(f"{position:4}. {user}: {counter} veces")

        position += 1


def recover_repository(repo_URL, repo_directory_name):
    if os.path.isdir(repo_directory_name):
        repo = git.Repo(repo_directory_name)
        repo.remote().fetch
    else:
        os.mkdir(repo_directory_name)
        repo = git.Repo.clone_from(repo_URL, repo_directory_name)

    return repo


def get_ranking(base_path):
    ranking = {}

    for _, _, files in os.walk(base_path):
        for file in files:
            user_name, extension = os.path.splitext(file)
            if extension != ".md":
                ranking[user_name] = ranking.get(user_name, 0) + 1

    sorted_ranking = dict(
        sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    )

    return sorted_ranking


if __name__ == "__main__":
    main()
