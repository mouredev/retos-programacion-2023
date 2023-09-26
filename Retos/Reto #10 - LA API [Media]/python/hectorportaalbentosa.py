import requests as req
import json


"""
Desarrollo de consultor rápido de nombre e id del pokémon.
"""

def mostrarPokemon(pkm):
    nombre = pkm["name"]
    id = str(pkm["id"])
    print("El pokemon que ha buscado es "+ nombre + " y su id es "+ id)



def parserJson(texto):
    return json.loads(texto)

if __name__ == "__main__":
    url = "https://pokeapi.co/api/v2/pokemon/"
    while True:
        pkm = input("Dime el nombre o numero del pokémon que buscas: ")
        if pkm != "":
            break     
    a = req.get(url+pkm)
    try:
        if a.status_code == 404:
            a.raise_for_status()
        else:
            pkm = parserJson(a.content)
            mostrarPokemon(pkm)
    except req.exceptions.HTTPError:
        print("Eres peor que un juego de pokémon de la switch, escribe bien la id o el nombre del pokémon!!!")
    
