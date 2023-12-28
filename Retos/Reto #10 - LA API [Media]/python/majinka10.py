import requests, json

class pokemon:
    def __init__(self, nombre:str, stats:dict, abilitiies:list, forms:list, moves:list):
        self.nombre=nombre
        self.stats=stats
        self.abilities=abilitiies
        self.forms=forms
        self.moves=moves

#El número '5' en la url se puede cambiar hasta 1281
url = 'https://pokeapi.co/api/v2/pokemon?limit=5&offset=0'
response = requests.get(url).json()

pokemones = response.get('results')
pokemons_list=[]

for pokecall in pokemones:
    nombre = pokecall.get('name').capitalize()
    url_pokemon = pokecall.get('url')
    response_pokemon = requests.get(url_pokemon).json()
    abilities = response_pokemon.get('abilities')
    stats = response_pokemon.get('stats')
    forms = response_pokemon.get('forms')
    moves = response_pokemon.get('moves')
    abilities_list=[]
    forms_list=[]
    stats_list={}
    moves_list=[]
    for ability in abilities:
        nombre_habilidad = ability.get('ability').get('name').capitalize()
        abilities_list.append(nombre_habilidad)
    for form in forms:
        nombre_forma = form.get('name').capitalize()
        forms_list.append(nombre_forma)
    for stat in stats:
        nombre_stat=stat.get('stat').get('name').capitalize()
        stats_list[nombre_stat]=stat.get('base_stat')
    for move in moves:
        nombre_movimiento= move.get('move').get('name').capitalize()
        moves_list.append(nombre_movimiento)
    pokemon_object = pokemon(nombre,stats_list,abilities_list,forms_list,moves_list)
    pokemons_list.append(pokemon_object)

for poke in pokemons_list:
    print(f"Nombre del pokemón: {poke.nombre}\n")
    print(f"Estadísticas: {poke.stats}")
    print(f"Habilidades: {poke.abilities}")
    print(f"Movimientos: {poke.moves}")
    print(f"Formas: {poke.forms}\n")