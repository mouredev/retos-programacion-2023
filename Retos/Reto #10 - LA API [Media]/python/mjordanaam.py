"""
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
import json

URL = "https://api.vatcomply.com/currencies"

response = requests.get(URL)

currencies = json.loads(response.text)

print("List of currencies: \n")

for key, values in currencies.items():
	print(key)
	print("NAME: " + values['name'])
	print("SYMBOL: " + values['symbol'] + "\n")
