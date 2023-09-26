def obtener_sublistas(longitud: int, objetivo: int) -> list:
    return []


def sumas(lista: list, objetivo: int) -> list:
    resultado = list()

    lista = list(filter(lambda x: x <= objetivo, lista))

    for n in range(1, len(lista)+1):
        resultado += obtener_sublistas(n, objetivo)

    return resultado


resultado = sumas([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(resultado)
