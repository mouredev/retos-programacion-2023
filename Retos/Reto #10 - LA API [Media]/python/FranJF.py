# /*
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs: 
#  * https://github.com/public-apis/public-apis
#  */

import requests

def buscar_pokemon():
    print("Introduce el nombre del Pokemon a buscar")
    pokemon = input()
    url:str = "https://pokeapi.co/api/v2/pokemon/"+pokemon
    response=requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("No hemos encontrado ese Pokemon, prueba con otro")
        buscar_pokemon()

print(buscar_pokemon())
