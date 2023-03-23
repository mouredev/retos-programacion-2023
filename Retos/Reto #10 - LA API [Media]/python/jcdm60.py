import requests


def obtiene_pokemon(cantidad):

    url = "https://pokeapi.co/api/v2/pokemon"
    limite_maximo = {"limit": cantidad}

    respuesta = requests.get(url, params=limite_maximo)

    if respuesta.status_code == 200:
        pokemon_data = respuesta.json()
        for pokemon in pokemon_data["results"]:
            print(pokemon["name"])
    else:
        print("No se pudo conectar a la API de Pokémon.")
    respuesta = requests.get(url)


if __name__ == "__main__":
    cantidad = int(input("Ingresa un número entero: "))
    obtiene_pokemon(cantidad)
