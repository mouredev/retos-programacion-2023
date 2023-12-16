# * Todo llega a su fin... Este es el último reto de programación
#  * semanal de 2023.
#  *
#  * Crea un programa que muestre un listado calculado en tiempo real
#  * con todos los usuarios que han resuelto algún reto de programación
#  * de este año.
#  * - El listado debe estar ordenado por el número de ejercicios resueltos
#  *   por cada usuario (y mostrar ese contador al lado de su nombre).
#  * - También se debe de mostrar el número de usuarios que han participado
#  *   y el número de correcciones enviadas.
#  *
#  * Muchísimas gracias por ayudar a crear este gran recurso
#  * para la comunidad... ¡Prepárate para 2024!

from github import Github


def listUsers():
    g = Github()
    repo = g.get_repo('MoureDev/retos-programacion-2023')
    users = list()
    for i in repo.get_contributors():
        users.append([i.login, i.contributions])

    return users


if __name__ == '__main__':
    users = listUsers()
    for i in users:
        user, contributions = i
        print(f'Usuario: {user}, Contribuciones: {contributions}')
