"""
#  * Llamada usando libreria requests a la api con url https://pokeapi.co/api/v2/pokemon/
"""

import requests


def apiCall(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        print(data)
    else:
        print(f"Error al llamar a la API: {response.status_code}")


id = input("Enter name or id of the pokemon: ")
apiCall(id)