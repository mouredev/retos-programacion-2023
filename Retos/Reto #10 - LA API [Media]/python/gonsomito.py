"""
 * Llamar a una API es una de las tareas más comunes en programación.
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
"""
import requests              # requiere  instalar modulo con : pip install requests

respuesta = requests.get("https://www.thesportsdb.com/api/v1/json/3/all_leagues.php")

print(respuesta)
