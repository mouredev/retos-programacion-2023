import requests

def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

    # Realizar la solicitud GET a la API
    response = requests.get(url)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:  # 200 significa éxito
        # Mostrar la información obtenida en formato JSON
        data = response.json()
        print(f"Información de {pokemon_name.capitalize()}:")
        print(f"Nombre: {data['name']}")
        print(f"ID: {data['id']}")
        print("Habilidades:")
        for ability in data['abilities']:
            print(f"- {ability['ability']['name']}")
    else:
        print(f"Error al obtener datos de {pokemon_name}. Código de estado: {response.status_code}")

def main():
    pokemon_list = ['pikachu', 'charmander', 'squirtle', 'bulbasaur', 'jigglypuff', 'eevee', 'magikarp', 'snorlax']

    for pokemon in pokemon_list:
        get_pokemon_info(pokemon)
        print("")

if __name__ == "__main__":
    main()
