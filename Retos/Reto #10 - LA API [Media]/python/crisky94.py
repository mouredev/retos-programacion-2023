# /*
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs: 
#  * https://github.com/public-apis/public-apis
#  */

import requests as req # type: ignore

url = 'https://api.thecatapi.com/v1/images/search'
response = req.get(url)
data = response.json()
print(data)

