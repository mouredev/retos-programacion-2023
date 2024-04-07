#!/usr/bin/python3

"""
# Reto #48: El ranking
/*
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
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


import os
import json

from collections import Counter

import requests
import pandas as pd 


USER = 'mouredev'
REPO = 'retos-programacion-2023'
BRANCH = 'main'
FILES_GITHUB = f'https://api.github.com/repos/{USER}/{REPO}/git/trees/{BRANCH}?recursive=1'


def paso1_obtener_datos():
    # se obtiene la data de la api de github
    data = None
    try:
        req = requests.get(FILES_GITHUB)
        data = req.json()
        # print(json.dumps(data, indent=2))
    except:
        pass
    return data


def paso_2_obtener_archivos_extensiones(data):
    # se leen los archivos
    # se toma el valor tree del json
    tree_list = data["tree"] 
    # dentro de cada item se tooma el la ruta de los archivos
    list_paths = [ item["path"] for item in tree_list]
    # se separa la ruta para obtener el basename
    list_paths = [ item.split("/") for item in list_paths ]
    # se hace un filtrado para evitar errores de indice
    list_paths = [ item for item in list_paths if len(item) == 4 ]
    # se toma el basename que contiene el nombre de usuario junto con la extension
    list_basename = [ item[3] for item in list_paths ]
    # se separa el nombre de usuario de la extension en cada item
    list_split_ext = [ os.path.splitext(item) for item in list_basename ]
    return list_split_ext


def paso_3_agrupar_extensiones(list_split_ext):
    """
    Esta es mi contribucion especial para este ejercicio, 
    esta funcion es capaz de calcular que contribucion ha hecho cada usuario en
    los diferentes lenguajes (extensiones de archivos)
    """
    #
    df = pd.DataFrame(list_split_ext, columns =['username', 'language'])
    df["language"] = df["language"].str.replace(".", "", regex=False) 
    df_grouped = df.groupby(["username", "language"]).size().reset_index(name='count') 
    #
    df_grouped = df_grouped.groupby('username').apply(lambda x: x.groupby('language')\
                 .apply(lambda x: int(x[['count']].iloc[0,0])).to_dict()).to_dict()
    #
    total_records = df.groupby("username")["language"].count().reset_index(name="count")\
            .sort_values(['count'], ascending=False).to_dict('records')
    #
    total_records = [ aux_total_languages(item, df_grouped[item["username"]]) for item in total_records ]
    return total_records



def aux_total_languages(dict1, dict2):
    # print(dict1)
    # print(dict2)
    out = {
        "username": dict1["username"], 
        "language": dict2, 
        "count": dict1["count"]
    }
    return out


def paso_4_agrupar_sin_extensiones(list_split_ext):
    # esta es una forma mas rapida de obtener la salida que se nos pide
    df = pd.DataFrame(list_split_ext, columns =['username', 'language'])
    total_df = df.groupby("username")["language"].count().reset_index(name="count")\
                .sort_values(['count'], ascending=False)
    return total_df.to_dict('records')


def main():
    data = paso1_obtener_datos()
    list_paths = paso_2_obtener_archivos_extensiones(data)
    output = paso_3_agrupar_extensiones(list_paths)
    for i,item in enumerate(output):
        print(i, "\t", "Usuario: ", item["username"], "\t", "numero de retos resuletos: ", item["count"])
    print("numero total de usuarios:", len(output))


if __name__ == '__main__':
    main()
