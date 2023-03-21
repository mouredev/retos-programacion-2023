"""

 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis

"""

import requests


def api(id):
    if id > 100:
        return "El id no puede ser mayor a 100"
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(f'{url}/{id}')

        body = f'Usuario Id: {response.json()["userId"]}\nId: {response.json()["id"]}\nTitulo: {response.json()["title"]}\nCuerpo: {response.json()["body"]}'
        return body
    except:
        return "El id no existe"


print(api(101))
