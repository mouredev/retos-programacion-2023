import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> str:
    if url is None:
        raise SystemExit() from None
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err) from None
    return response.text


def get_schedule(doc: str, text: str = " Agenda 8 de mayo | ") -> list:
    title = doc.find_all(string=text)[0].find_parent("h1")
    return [appointment.get_text() for appointment in title.find_all_next("blockquote")]


def main():
    url = "https://holamundo.day/"
    doc = BeautifulSoup(get_html(url), "html.parser")
    appointments = get_schedule(doc)
    for appointment in appointments:
        print(appointment)


if __name__ == "__main__":
    main()
