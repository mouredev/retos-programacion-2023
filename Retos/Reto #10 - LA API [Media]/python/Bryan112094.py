# Llamar a una API es una de las tareas más comunes en programación.
# Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
# resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
# Aquí tienes un listado de posibles APIs: 
# https://github.com/public-apis/public-apis

import requests, json

def buscar_id_pokemon(pokemon):
    link = 'https://pokeapi.co/api/v2/pokemon/'
    res_api = requests.get(link + pokemon)
    if res_api.status_code == 200:
        result = json.loads(res_api.content)
        print(f"Tu pokemon {result['name']} tiene de ID: {result['id']}")
    else:
        print("Pokemon no encontrado en la pokedex")

buscar_id_pokemon('charmader')
