import requests

url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
response = requests.get(url)
data = response.json()["results"]
for i in data:
    pokemon_name = i["name"]
    pokemon_url = i["url"]
    print(pokemon_name, pokemon_url)