import requests


def get_player(id: str) -> str:
    url = "https://www.balldontlie.io/api/v1/players/"
    response = requests.get(url+id)

    if response.status_code == 200:
        data = response.json()
        
        name = data["first_name"]
        last_name = data["last_name"]
        team = data["team"]["full_name"]

        return f"{name} {last_name}, {team}"
    
    else:
        return "Error en la consulta de la API."


if __name__ == "__main__":
    id = input("Ingrese el Id del jugador a consultar: ")
    player = get_player(id)
    print(player)
