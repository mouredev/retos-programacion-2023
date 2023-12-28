"""/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */"""

import requests


def ask_airport_departure():
    return input("Aeropuerto (Ej. HND,SIN): ")


def check_by_airport_departure(airport_departure, api_response):
    for flight in api_response["data"]:
        if airport_departure in (flight["departure"]["iata"]):
            print(
                f"Vuelo: {flight['airline']['name']} {flight['flight']['iata']} con destino a: {flight['arrival']['airport']}, \n Estado del Vuelo: {flight['flight_status'].capitalize()} \n Hora de Salida {flight['departure']['scheduled'].split('T')[1]} \n"
            )


def main():
    params = {"access_key": "82bfcf355f0bb92c1ca10dcac3d4025c"}
    api_result = requests.get("http://api.aviationstack.com/v1/flights", params)

    api_response = api_result.json()

    airport_departure = ask_airport_departure()
    check_by_airport_departure(airport_departure, api_response)


if __name__ == "__main__":
    main()
