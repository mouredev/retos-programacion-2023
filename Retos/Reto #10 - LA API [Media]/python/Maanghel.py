"""
Llamar a una API es una de las tareas más comunes en programación.

Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...

Aquí tienes un listado de posibles APIs:
https://github.com/public-apis/public-apis
"""

from typing import List, Dict
import requests

URL: str = "https://digimon-api.vercel.app/api/digimon"

def fetch_digimons(url: str) -> List[Dict[str, str]]:
    """
    Fetch Digimon data from the given API URL.

    Args:
        url (str): API endpoint.

    Returns:
        List[Dict[str, str]]: List of digimons with their attributes.

    Raises:
        requests.RequestException: If there is a network or HTTP error.
        ValueError: If data is not a list.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, list):
            raise ValueError("Formato de respuesta de la API inesperado.")

        return data
    except (requests.RequestException, ValueError) as e:
        print(f"Error obteniendo datos: {e}")
        return []

def display_digimons(digimons: List[Dict[str, str]]) -> None:
    """
    Print digimon names and levels to the console.

    Args:
        digimons (List[Dict[str, str]]): List of digimons to display.
    """
    for index, digimon in enumerate(digimons, 1):
        name = digimon.get("name", "Unknown")
        level = digimon.get("level", "Unknown")
        print(f"\nIndex: {index}\nNombre: {name}\nNivel: {level}")


if __name__ == "__main__":
    digimons = fetch_digimons(URL)
    display_digimons(digimons)
