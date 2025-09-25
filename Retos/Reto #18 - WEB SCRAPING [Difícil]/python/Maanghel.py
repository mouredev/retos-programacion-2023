"""
El día 128 del año celebramos en la comunidad el "Hola Mundo day"
    Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day

Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
    del día 8. Mostrando hora e información de cada uno.
Ejemplo: "16:00 | Bienvenida"

Se permite utilizar librerías que nos faciliten esta tarea.
"""

import re
from bs4 import BeautifulSoup
import requests

URL = "https://holamundo.day"
EVENT_CLASS = "rt-Text rt-r-size-4"
TIME_PATTERN = re.compile(r"^(?:[01]\d|2[0-3]):[0-5]\d$")

def get_html(url: str) -> str:
    """
    Realiza una petición HTTP a la URL especificada y devuelve el contenido HTML.

    Parámetros:
        url (str): Dirección web a la que se realizará la solicitud.

    Retorna:
        str: El contenido HTML de la página.

    Lanza:
        ConnectionError: Si ocurre un problema de red o conexión.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"No se pudo conectar a {url}.") from e

def get_events(html: str) -> list[tuple[str, str]]:
    """
    Procesa el HTML de la página y extrae los eventos del día 8.

    Parámetros:
        html (str): Contenido HTML de la página.

    Retorna:
        list[tuple[str, str]]: Lista de tuplas (hora, descripción).

    Lanza:
        ValueError: Si no se encuentra la estructura esperada en la página.
    """
    soup = BeautifulSoup(html, "html.parser")
    eventos_span = soup.find_all("span", class_=EVENT_CLASS)

    if not eventos_span:
        raise ValueError("No se encontro la estructura de eventos en la página.")

    eventos = []
    for span in eventos_span:
        strong = span.find("strong")
        if strong:
            hora = strong.get_text(strip=True)
            descripcion = span.get_text(strip=True).replace(hora, "", 1).strip()
            if TIME_PATTERN.fullmatch(hora):
                eventos.append((hora, descripcion))

    return eventos

def print_events(eventos: list[tuple[str, str]]) -> None:
    """
    Imprime la lista de eventos en formato legible.

    Parámetros:
        eventos (list[tuple[str, str]]): Lista de tuplas (hora, descripción).
    """
    if not eventos:
        print("No se encontraron eventos en la agenda.")
        return

    for hora, descripcion in eventos:
        print(f"{hora} | {descripcion}")


def get_agenda_day8() -> None:
    """
    Función principal: obtiene e imprime la agenda de eventos del día 8.
    Maneja excepciones y muestra mensajes claros al usuario.
    """
    try:
        html = get_html(URL)
        events = get_events(html)
        print_events(events)
    except (ConnectionError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    get_agenda_day8()
