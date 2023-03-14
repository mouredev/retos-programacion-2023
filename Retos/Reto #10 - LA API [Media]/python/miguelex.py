import requests

url = 'https://swapi.dev/api/people/'
next_url = url
count = 1

while next_url:
    response = requests.get(next_url)

    if response.status_code == 200:
        data = response.json()

        for person in data['results']:
            print(f'Personaje Nº: {count}')
            print(f'Nombre: {person["name"]}')
            print(f'Año de nacimiento: {person["birth_year"]}')
            print(f'Genero: {person["gender"]}')
            print(f'Lugar de origen: {person["homeworld"]}')
            print("-----------------------------------")
            count += 1

        next_url = data['next']
    else:
        print(
            f'Error al hacer la solicitud. Código de respuesta: {response.status_code}')
        break
