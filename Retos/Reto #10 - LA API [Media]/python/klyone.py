#!/usr/bin/env python3

import requests

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"


def request_pokemon_info(pokemon):
    pokemon_info = requests.get(POKEAPI_URL + pokemon)
    print(pokemon_info.json())


if __name__ == "__main__":
    request_pokemon_info("pikachu")
    request_pokemon_info("charmander")
    request_pokemon_info("rattata")
