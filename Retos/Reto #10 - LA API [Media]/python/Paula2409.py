"""/*
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

def request_http():
    request = requests.get('https://developer.oxforddictionaries.com/')
    print(request.status_code) # prints 200 (ok)
    print(request.headers) # print(headers of API)
    print(request.json) # <bound method Response.json of <Response [200]>>
    print(request.text) # text HTML and CSS
    
request_http()