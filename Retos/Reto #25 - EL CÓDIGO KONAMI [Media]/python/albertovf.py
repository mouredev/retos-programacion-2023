class KEYS:
    ARRIBA = "arriba"
    ABAJO = "abajo"
    IZQUIERDA = "izquierda"
    DERECHA = "derecha"
    A = "a"
    B = "b"


def isKonami(entrada:[str]):
    entrada = list(map(lambda x: x.lower(), entrada))
    codigo_konami = [ KEYS.ARRIBA, KEYS.ARRIBA, KEYS.ABAJO, KEYS.ABAJO, KEYS.IZQUIERDA, KEYS.DERECHA, KEYS.IZQUIERDA, KEYS.DERECHA, KEYS.B, KEYS.A, ]

    return entrada == codigo_konami


def reto():
    entrada = input('Introduce el codigo coname con letras: ')
    print(isKonami(entrada.split(' ')))

reto()