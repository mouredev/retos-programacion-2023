from random import choice, randint, sample
from os import *

longitud_palabra = ""

def inicio():
    system("cls")
    words = ['LAPTOP', 'CELULAR', 'JIRAFA', 'PYTHON', 'GATO', 'MESSI', 'GOAT']
    global longitud_palabra
    print('ADIVINA LA PALABRA')
    palabra_seleccionada = choice(words)
    longitud_palabra = len(palabra_seleccionada)
    palabra_adivinanza = list("_" * longitud_palabra)
    
    # Se delimita las letras mostradas y selecciona indices que se mostraran
    num_letras_mostradas = randint(2, longitud_palabra//2)
    posiciones_mostradas = sample(range(longitud_palabra), num_letras_mostradas)
    
    # Reemplazar los guiones bajos en las posiciones seleccionadas con las letras correspondientes
    for i in posiciones_mostradas:
        palabra_adivinanza[i] = palabra_seleccionada[i]

    juego(palabra_seleccionada, palabra_adivinanza)


def juego(palabra_seleccionada, palabra_adivinanza):
    intentos = 6

    while True:

        espacios = 0
        print("INTENTOS DISPONIBLES: ", intentos)
        print(" ".join(palabra_adivinanza))
        dibujo(intentos)

        for i in range(longitud_palabra):
            if palabra_adivinanza[i] == '_':
                espacios += 1

        if espacios == 0 and intentos != 0:
            print('has ganado bien jugado')
            system("pause")
            inicio()
        
        elif intentos == 0:
            print('Haz perdido')
            system("pause")
            inicio()
        
        texto = input('Escribe una letra o la palabra: ').upper()


        if len(texto) == 1:

            if texto in palabra_seleccionada:
                i = palabra_seleccionada.find(texto)
                palabra_adivinanza[i] = palabra_seleccionada[i]
            else:
                intentos -= 1

        elif len(texto) == longitud_palabra:

            if texto == palabra_seleccionada:
                palabra_adivinanza = palabra_seleccionada
            else:
                intentos -= 1

        else:
            intentos -= 1



def dibujo(intentos):

    if intentos == 6:
        print("\n     _______\n    |       |\n    |\n    |\n    |\n    |\n    |\n ----------")
    elif intentos == 5:
        print("\n     _______\n    |       |\n    |       0\n    |\n    |\n    |\n    |\n ----------")
    elif intentos == 4:
        print("\n     _______\n    |       |\n    |       0\n    |       |\n    |\n    |\n    |\n ----------")
    elif intentos == 3:
        print("\n     _______\n    |       |\n    |       0\n    |      /|\n    |\n    |\n    |\n ----------")
    elif intentos == 2:
        print("\n     _______\n    |       |\n    |       0\n    |      /|\ \n    |\n    |\n    |\n ----------")
    elif intentos == 1:
         print("\n     _______\n    |       |\n    |       0\n    |      /|\ \n    |      /\n    |\n    |\n ----------")
    elif intentos == 0:
         print("\n     _______\n    |       |\n    |       0\n    |      /|\ \n    |      / \ \n    |\n    |\n ----------")


inicio()