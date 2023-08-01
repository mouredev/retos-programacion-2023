import os
import operator


def scan_dir(dir_path, challenges={}, languages={}, users={}, total=0, challenge_name=None, path_name=None) -> tuple:
    for path in os.scandir(dir_path):
        if path.is_dir():
            if "Reto #" in path.name and path.name not in challenges:
                challenges[path.name] = 0
                challenge_name = path.name
            elif "Reto #" not in path.name and path.name not in languages:
                languages[path.name] = 0
            elif "Reto #" not in path.name and path.name not in users:
                users[path.name] = 0

            _, _, _, total = scan_dir(path.path, challenges, languages, users, total, challenge_name, path.name)

        if path_name in languages:
           total += 1
           if challenge_name is not None:
              challenges[challenge_name] += 1
              languages[path_name] += 1
     
        if path_name in users:
           total += 1
           if challenge_name is not None:
              challenges[challenge_name] += 1
              users[path_name] += 1
    return (challenges, languages, users, total)


# Directorio de retos a analizar
dir_path = os.path.dirname(__file__)

# Directorio de un reto específico
# dir_path = "Reto #30 - EL TECLADO T9 [Media]"

# Función recursiva para recorrer el directorio y almacenar el número de archivos por reto y lenguaje
challenges, languajes, users, total = scan_dir(dir_path)

# Ordenación por uso
challenges = dict(
    sorted(challenges.items(), key=operator.itemgetter(1), reverse=True))
languajes = dict(
    sorted(languajes.items(), key=operator.itemgetter(1), reverse=True))
users = dict(
    sorted(users.items(), key=operator.itemgetter(1), reverse=True))

# Estadísticas
print(
    f"\nESTADÍSTICAS RETOS DE PROGRAMACIÓN:\n> {len(languajes.keys())} LENGUAJES ({total} CORRECCIONES)\n")
for challenge in challenges:
    print(
        f"> {challenge.upper()} ({challenges[challenge]}): {round(challenges[challenge] / total * 100, 2)}%")
print()
for languaje in languajes:
    print(
        f"> {languaje.upper()} ({languajes[languaje]}): {round(languajes[languaje] / total * 100, 2)}%")
print()
for user in users:
    print(
        f"> {user.upper()} ({users[user]}): {round(users[user] / total * 100, 2)}%")