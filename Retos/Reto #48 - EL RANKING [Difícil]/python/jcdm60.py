# Reto #48: El ranking
#### Dificultad: Difícil | Publicación: 11/12/23 | Corrección: 18/12/23

## Enunciado

#
# Todo llega a su fin... Este es el último reto de programación 
# semanal de 2023.
#
# Crea un programa que muestre un listado calculado en tiempo real
# con todos los usuarios que han resuelto algún reto de programación
# de este año.
# - El listado debe estar ordenado por el número de ejercicios resueltos
#   por cada usuario (y mostrar ese contador al lado de su nombre).
# - También se debe de mostrar el número de usuarios que han participado
#   y el número de correcciones enviadas.
#
# Muchísimas gracias por ayudar a crear este gran recurso
# para la comunidad... ¡Prepárate para 2024!   
#

import os
import time
from collections import Counter

class FileLister:
    def __init__(self):
        self.archivos_encontrados = []  # Lista para almacenar nombres de archivos

    def listar_archivos_tres_niveles_con_delay(self, ruta, nombre_archivo=None, nivel=0):
        # Verifica si la ruta es válida
        if os.path.exists(ruta) and os.path.isdir(ruta):
            # Verifica si hemos alcanzado tres niveles de profundidad
            if nivel <= 3:
                elementos = os.listdir(ruta)

                for elemento in elementos:
                    ruta_completa = os.path.join(ruta, elemento)
                    # Si es un directorio, llamamos recursivamente a la función con un nivel más profundo
                    if os.path.isdir(ruta_completa):
                        self.listar_archivos_tres_niveles_con_delay(ruta_completa, nombre_archivo, nivel + 1)
                    else:
                        # Si no se proporciona un nombre de archivo o coincide con el nombre buscado, se agrega a la lista
                        nombre_archivo_encontrado = os.path.splitext(os.path.basename(ruta_completa))[0]
                        if not nombre_archivo or nombre_archivo_encontrado == nombre_archivo:
                            if not ruta_completa.endswith('.md'):
                                self.archivos_encontrados.append(nombre_archivo_encontrado)

        else:
            print("La ruta no es válida o no es un directorio.")

    def obtener_total_archivos(self):
        return len(self.archivos_encontrados)

    def obtener_total_archivos_diferentes(self):
        return len(set(self.archivos_encontrados))

    def imprimir_conteo_archivos(self):
        conteo_archivos = Counter(self.archivos_encontrados)

        # Imprime la lista de nombres de archivos recolectados (sin extensión) con su respectivo conteo en orden descendente
        delay = 0.1
        for archivo, cantidad in conteo_archivos.most_common():
            print(f"{archivo} - Total: {cantidad}")
            time.sleep(delay)

if __name__ == '__main__':
    # Crear una instancia de la clase FileLister
    file_lister = FileLister()

    # Ruta del directorio principal "Retos"
    dir_path = 'D:\\Retos_semanales_2023\\retos-programacion-2023\\Retos\\'

    # Pedir al usuario que ingrese el nombre del archivo (sin extensión)
    nombre_archivo_buscado = input("Ingrese el nombre del archivo (sin extensión) o deje vacío para listar todos los archivos: ")

    # Llama a la función para listar archivos dentro de tres niveles de directorios
    file_lister.listar_archivos_tres_niveles_con_delay(dir_path, nombre_archivo_buscado)

    # Obtiene el total de archivos y el total de archivos diferentes (excluyendo .md)
    total_archivos = file_lister.obtener_total_archivos()
    total_archivos_diferentes = file_lister.obtener_total_archivos_diferentes()

    print(f"Total de correcciones enviadas: {total_archivos}")
    print(f"Total de usuarios que han participado: {total_archivos_diferentes}")
    print("-" * 40)  # Línea separadora

    # Imprimir conteo de archivos
    file_lister.imprimir_conteo_archivos()












    














