import requests
import json

URL = "https://pokeapi.co/api/v2/pokemon/1"

response = requests.get(URL)
pokemon = json.loads(response.text)
nombre = pokemon.get('name').capitalize()

print("Mi pokemon favorito es de la primera generacion es " + nombre)

