""" 
 * Crea un programa que muestre un listado calculado en tiempo real
 * con todos los usuarios que han resuelto algún reto de programación
 * de este año.
 * - El listado debe estar ordenado por el número de ejercicios resueltos
 *   por cada usuario (y mostrar ese contador al lado de su nombre).
 * - También se debe de mostrar el número de usuarios que han participado
 *   y el número de correcciones enviadas. 
 """
import os
from collections import Counter

current_directory = os.path.dirname(os.path.abspath(__file__))

grandparent_directory = os.path.abspath(os.path.join(current_directory, os.pardir, os.pardir))

def get_file_names_in_subdirectories(directory):
    file_names = []

    for current_directory, subdirectories, files in os.walk(directory):
        for file in files:

            name_without_extension = os.path.splitext(file)[0]
            if name_without_extension == 'ejercicio' or name_without_extension == 'language_stats':
                continue
            # Add the file name to the list
            file_names.append(name_without_extension)

    return file_names

file_names = get_file_names_in_subdirectories(grandparent_directory)

counter = Counter(file_names)

sorted_files  = sorted(counter.items(), key=lambda x: x[1], reverse=True)

participants = len(set(file_names))
total_corrections = len(file_names)

print("\nRanking top 20:\n")
for file, repetitions in sorted_files[0:20]:
    print(f"{file}: {repetitions} repetitions")

print(f"\nNumber of participants: {participants}\n")
print(f"Total number of corrections sent: {total_corrections}\n")

