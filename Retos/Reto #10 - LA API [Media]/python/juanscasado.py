# /*
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs: 
#  * https://github.com/public-apis/public-apis
#  */

import requests

# hacemos la request por el metodo http: get
r = requests.get("https://meowfacts.herokuapp.com")

# asignamos variable data a la data del json
data = r.json()['data']

# imprimimos da data con el * para sacarla nde su arreglo
print(*data)