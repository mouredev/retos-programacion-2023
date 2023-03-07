"""
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
"""

import requests     # pip install requests
import pprint       # para ver mejor los datos

pokemon_name = input("Enter a Pokemon name: ")
r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")

pprint.pprint(r.json())