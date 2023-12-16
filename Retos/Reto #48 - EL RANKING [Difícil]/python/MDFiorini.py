import os
import requests

BASE_URL = 'https://github.com/mouredev/retos-programacion-2023/tree/main/'
users = {}
correcciones = 0


def do_request(path):
    url = (BASE_URL + path).replace(' ', '%20').replace('#', '%23').replace('[', '%5B').replace(']', '%5D')
    response = requests.get(url, timeout=2)
    return response


def get_items(path):
    response = do_request(path)
    items = response.json()['payload']['tree']['items']
    return items


os.system('cls') # Windows

retos = get_items('Retos')
retos.pop()

for reto in retos:
    languages = get_items(reto['path'])
    languages.pop()
    print(reto['name'])
    for language in languages:
        users_list = get_items(language['path'])
        print(f'    {language["name"]} - {len(users_list)}')
        for user in users_list:
            username = user["name"].split('.')[0]
            if username not in users:
                users[username] = 1
            else:
                users[username] += 1
    print()

oreder_list = sorted(users.items(), key=lambda item: item[1], reverse=True)

for user, value in oreder_list:
    print(f'{user} - {value}')
    correcciones += value

print(f'''
Usuarios totales: {len(oreder_list)}
Correcciones    : {correcciones}
      ''')
