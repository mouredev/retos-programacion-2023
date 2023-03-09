"""
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs: 
#  * https://github.com/public-apis/public-apis
"""

import requests


def apiCall(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        print(data)
    else:
        print(f"Error al llamar a la API: {response.status_code}")


id = input("Enter name or id of the pokemon: ")
apiCall(id)
