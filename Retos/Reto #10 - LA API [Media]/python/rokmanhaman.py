"""
Reto #10: LA API
/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */
 """

import requests

url = "https://www.fruityvice.com/api/fruit/all"


response = requests.get(url)


for fruit in response.json():
    print(f"{fruit['name']} --- {fruit['family']}")
