'''
 Llamar a una API es una de las tareas más comunes en programación.

 Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...

 Aquí tienes un listado de posibles APIs: 
 https://github.com/public-apis/public-apis
'''

import requests


def getFreeGames(list_size: int = 20) -> list:
    games = []

    try:
        request = requests.get(
            'https://www.freetogame.com/api/games')

        if request.status_code == 200:
            json_data = request.json()[0:list_size]

            for game in json_data:
                games.append(f'{game["title"]}: {game["platform"]}')

        else:
            print('No se pudo hacer la consulta. Respuesta:', request.status_code)

    except requests.exceptions.RequestException as e:
        print("Ocurrió un error al hacer una consulta a la API:", str(e))

    finally:
        return games


if __name__ == '__main__':
    games = getFreeGames()
    print(*games, sep='\n')
