import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=151"

response = requests.get(url)

for index, pokemon in enumerate(response.json()["results"]):
    pokemon_name = pokemon["name"]
    print(f"#{index + 1} {pokemon_name}")
