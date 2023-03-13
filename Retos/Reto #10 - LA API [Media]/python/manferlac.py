# API: https://openlibrary.org/dev/docs/api/books#
# Example ISBN:
# 9780140328721
# 0486283534
# Puedes encontrar más libros en: https://openlibrary.org/

import requests

API_URL = "https://openlibrary.org/isbn/<isbn_code>.json"


def getBook(isbn):
    url = API_URL.replace("<isbn_code>", isbn)
    response = requests.request("GET", url)
    if response.status_code != 200:
        print("No se ha encontrado el libro")
    else:
        book = response.json()
        print(f"Título: {book['title']}")
        print(f"Fecha publicación: {book['publish_date']}")
        print(f"Número de páginas: {book['number_of_pages']}")
        print(f"Revisiones: {book['revision']}")
        print("Idiomas:")
        for i in book['languages']:
            lan = i['key'].replace("/languages/", "")
            print(f" - {lan}")


if __name__ == '__main__':
    print("--- Buscador de libros por ISBN: ---")
    isbn = input("Por favor, introduce un ISBN:")
    getBook(isbn)
