"""/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
 */
    """
import re
from typing import Generator


import requests
from bs4 import BeautifulSoup, Tag


def get_page_url(url: str) -> str:
    return url


def request_page(url: str) -> requests.Response:
    return requests.get(url=url)


def search_words(paterns: list[list[str]], text: str) -> list[list[str]]:
    return [[re.search(patern, text).group() for patern in list] for list in paterns]


def show_agenda(phrases: list[list[str]]) -> None:
    print("Agenda")
    phrases: Generator = (phrase for phrase in phrases)

    for phrase in phrases:
        print(phrase)


def convert_response_to_soup_obj(response: requests.Response) -> BeautifulSoup:
    return BeautifulSoup(response.content, "html.parser")


def find_tags(soup_obj: BeautifulSoup, tag: str, __class: str = None) -> list[Tag]:
    return soup_obj.find_all(tag, class_=__class)


def other_solution() -> None:
    url = get_page_url("https://holamundo.day")
    response: requests.Response = request_page(url)
    soup: BeautifulSoup = convert_response_to_soup_obj(response)

    results: list[Tag] = find_tags(
        soup, "blockquote", __class="BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width")

    print(">Agenda 8 de mayo | 'Hola Mundo' day")
    for activity in results[19:]:
        print(activity.text)


def main() -> None:
    other_solution()

    page_url: str = get_page_url("https://holamundo.day/")
    response: requests.Response = request_page(page_url)
    text: str = str(response.text)

    print("\n")
    phrases: list[list[str]] = search_words(text=text, paterns=[["16:00", "\|", "Bienvenida"], [
        "16:30", "\|", "De Junior a Junior: cómo abrirte paso", "\|", "Antonio Rodríguez"], ["17:00", "\|", "El Rol del Analista Funcional en el Ciclo de Desarrollo", "\|", "Luisina de Paula"], ["17:30", "\|", "Taller: Git y Github para el mundo", "\|", "Ehud Aguirre"], ["18:00", "\|", "Mesa redonda"], ["18:30", "\|", "Descanso \+ Sorteos"], ["19:00", "\|", "Clean Code: cómo dormir más y mejor", "\|", "Fran Sierra"], ["19:30", "\|", "Abrazando al fracaso", "\|", "Afor Digital"], ["20:00", "\|", "Taller: Descubre el mundo de machine learning", "\|", "Stefy Mojica"], ["20:30", "\|", "Elevator pitch"], ["21:00", "\|", "Invitados"], ["21:30", "\|", "Mi primer año como Desarrollador a los 45 años", "\|", "Gerardo Arrieta"], ["22:00", "\|", "Taller: Testing, más que código \| Manu Rodríguez"], ["22:30", "\|", "Descanso \+ Sorteos"], ["23:00", "\|", "Despedida"]])

    show_agenda(phrases)


if __name__ == "__main__":
    main()
