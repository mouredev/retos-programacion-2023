# Script para calcular el % de uso de cada lenguaje

import os
import operator


def scan_dir(dir_path, languages={}, total=0, path_name=None) -> tuple:
    for path in os.scandir(dir_path):
        if path.is_dir():
            if "Reto #" not in path.name and path.name not in languages:
                languages[path.name] = 0

            _, total = scan_dir(path.path, languages, total, path.name)
        else:
            if path_name in languages:
                total += 1
                languages[path_name] += 1

    return (languages, total)


# Directorio de retos a analizar
dir_path = os.path.dirname(__file__)
print(dir_path)
# Directorio de un reto específico
# dir_path += "/Reto #0 - EL FAMOSO FIZZ BUZZ [Fácil]"

# Función recursiva para recorrer el directorio y almacenar el número de archivos por lenguajes
languajes, total = scan_dir(dir_path)

# Ordenación por uso
languajes = dict(
    sorted(languajes.items(), key=operator.itemgetter(1), reverse=True))

# Estadísticas
print(f"{len(languajes.keys())} Lenguajes ({total} correcciones):")
for languaje in languajes:
    print(
        f"> {languaje.upper()} ({languajes[languaje]}): {round(languajes[languaje] / total * 100, 2)}%")
