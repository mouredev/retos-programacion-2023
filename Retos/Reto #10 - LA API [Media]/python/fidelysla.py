
#  * Llamar a una API es una de las tareas más comunes en programación.
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs:
#  * https://github.com/public-apis/public-apis

import requests

url = "https://pokeapi.co/api/v2/pokemon/?offset=150&limit=150"

response = requests.get(url=url)

text_results = response.json()["results"]
# dict_keys(['count', 'next', 'previous', 'results'])

for index, pokemon in enumerate(text_results):
    print(f"#{index+1}", pokemon["name"])
