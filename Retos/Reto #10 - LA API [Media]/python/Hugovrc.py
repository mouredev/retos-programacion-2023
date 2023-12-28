import requests
import json

def rick_morty_API(nombre):
    url = 'https://rickandmortyapi.com/api/character/?'
    args = {'name':nombre}

    respuesta = requests.get(url, params = args)
    #print(respuesta.url)

    if respuesta.status_code == 200:
        respuesta_json = json.loads(respuesta.text)
        resultado = respuesta_json.get('results', [])

        if resultado:
            for valores in resultado:
                nombre = valores['name']
                status = valores['status']
                genero = valores['gender']
                species = valores['species']

                print(f"\nNombre: {nombre}")
                print(f"Status: {status}")
                print(f"Genero: {genero}")
                print(f"Especie: {species}")
                
    else:
        print("No se pudo conectar con la API")

rick_morty_API("Rick")
#rick_morty_API("40 years old Morty")