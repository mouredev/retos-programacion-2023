"""
    Programa en el cual introduces una palabra, dependiendo las letras que contenga
    sumara una puntuación, si hace 100 puntos gana
"""

abecedario = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
              'N': 14, 'Ñ': 15, 'O': 16, 'P': 17, 'Q': 18, 'R': 19, 'S': 20, 'T': 21, 'U': 22, 'V': 23, 'W': 24, 'X': 25, 'Y': 26, 'Z': 27}


def jugar():
    print('******Hola bienvenido al juego de la palabra de los 100 puntos******')
    puntos: int = 0
    while puntos != 100:
        palabra: str = input('Introduce una palabra: ').upper()
        if palabra.isalpha():
            puntos = calcula_puntaje(palabra, puntos)
        else:
            print('Solamente se admiten letras')


def calcula_puntaje(palabra:str, puntos:int):
    for letra in palabra:
        for key, val in abecedario.items():
            if key == letra:
                puntos = puntos + val
    if puntos == 100:
        print(f'Perfecto lo lograste la palabra {
            palabra} tiene {puntos} de puntaje')
    else:
        print(f'Tu palabra "{palabra}" tiene {
            puntos} de puntaje, vamos intentalo de nuevo con otra palabra')
        puntos = 0
    return puntos


if __name__ == '__main__':
    jugar()
