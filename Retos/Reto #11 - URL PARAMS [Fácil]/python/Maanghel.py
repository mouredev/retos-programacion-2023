"""
Dada una URL con parámetros, crea una función que obtenga sus valores.
No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.

Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
los parámetros serían ["2023", "0"]
"""

from typing import List

def url_parameters(url: str) -> List[str]:
    """
    Extracts parameter values from a given URL string.

    Args:
        url (str): The input URL.

    Returns:
        List[str]: A list of parameter values found in the URL.

    Raises:
        TypeError: If the URL is not a string.
        ValueError: If the URL is empty.
    """
    _validate_url(url)

    parameters = []
    start = None
    for i, c in enumerate(url):
        if c == '?':
            start = i + 1
            break
    if start is None:
        return parameters

    current = start
    while current < len(url):
        eq_index = _search_eq_index(current, url)
        if eq_index is None:
            return parameters

        amp_index = _search_amp_index(eq_index, url)
        data = url[eq_index + 1: amp_index]
        parameters.append(data)
        current = amp_index + 1

    return parameters

def _search_eq_index(current_index: int, url: str) -> int | None:
    """
    Searches for the next '=' symbol in the URL starting from the given index.

    Args:
        current_index (int): The index to start searching from.
        url (str): The input URL.

    Returns:
        int | None: The index of '=' if found, otherwise None.
    """
    for i in range(current_index, len(url)):
        if url[i] == '=':
            return i
    return None

def _search_amp_index(eq_index: int, url: str) -> int:
    """
    Searches for the next '&' symbol in the URL starting after the '=' index.

    Args:
        eq_index (int): The index of the last '='.
        url (str): The input URL.

    Returns:
        int: The index of '&' if found, otherwise the length of the URL.
    """
    for i in range(eq_index + 1, len(url)):
        if url[i] == '&':
            return i
    return len(url)

def _validate_url(url: str) -> None:
    """
    Validates that the input is a non-empty string.

    Args:
        url (str): The URL to validate.

    Raises:
        TypeError: If the URL is not a string.
        ValueError: If the URL is empty.
    """
    if not isinstance(url, str):
        raise TypeError("La URL ingresada debe ser una cadena de texto.")
    if not url:
        raise ValueError("Debe ingresar una URL para proseguir.")


if __name__ == "__main__":
    URL: str = "https://retosdeprogramacion.com?year=2023&challenge=0"
    print(url_parameters(URL))
