import requests

def queryPokemon(pokemon: str) -> None:
    res = requests.get(
        f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    )
    if res.ok:
        name = res.json()['species']['name']
        type = res.json()['types'][0]['type']['name']
        weight = res.json()['weight']

        print(f'El Pokemon {name} es de tipo {type} y pesa {weight}')
    
    else:
        print(f'El Pokemon {pokemon} no se encuentra en la API.')

if __name__ == '__main__':
    queryPokemon('ditto')
    queryPokemon('pikachu')
    queryPokemon('charrizard')
