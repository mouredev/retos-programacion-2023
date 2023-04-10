from random import choice, randrange


def ocultarPalabra():
    global palabra, oculta

    oculta = list(palabra)

    for _ in range(int(len(palabra)*.6)):
        oculta[randrange(len(palabra))] = CARACTER_OCULTO

    oculta = ''.join(oculta)


def comprobarIntento(intento: str):
    global palabra, oculta, intentos

    if len(intento) == 1 and intento in palabra:
        oculta = ''.join([intento if intento == palabra[i] else oculta[i] for i in range(len(palabra))])
        return

    if intento == palabra:
        oculta = palabra
        return
    intentos -= 1


def reto():
    ocultarPalabra()
    while intentos > 0 and oculta != palabra:
        print(f'Intentos: {intentos}; Palabra: {oculta}')
        intento = input('introduce una letra o la solución: ').lower()
        comprobarIntento(intento)

    final = 'ganado' if oculta == palabra else 'perdido'
    print(f'\n¡Has {final}!\nLa palabra es "{palabra}"')


if __name__ == '__main__':
    intentos = 5
    palabras = ['esclavo', 'adulto', 'hoopla', 'rescate', 'ojos', 'animal', 'glacial', 'comadreja', 'sanitario', 'sonar', 'conflicto', 'hoja', 'hormonal', 'tarro', 'factual', 'conservador', 'todo', 'disruptor', 'dotante', 'sin', 'horror', 'flujo', 'feo', 'brazos',
                'conversacion', 'descubrimiento', 'desleal', 'pandemia', 'jade', 'chocante', 'pompa', 'pulpo', 'desmembramiento', 'sal', 'pistola', 'cortar', 'crisis', 'vacaciones', 'inverso', 'arrastrarse', 'redondo', 'felizmente', 'delicioso', 'bases', 'espada', 'jadeante']
    palabra = choice(palabras)
    CARACTER_OCULTO = "_"
    reto()
