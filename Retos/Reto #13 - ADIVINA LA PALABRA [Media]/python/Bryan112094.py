# Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
# - El juego comienza proponiendo una palabra aleatoria incompleta
#   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
# - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#   la palabra a adivinar)
#   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#     uno al número de intentos
#   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#     al número de intentos
#   - Si el contador de intentos llega a 0, el jugador pierde
# - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
# - Puedes utilizar las palabras que quieras y el número de intentos que consideres
import random

class adivinarPalabra:

    def __init__(self) -> None:
        pass

    def palabraRandom(self):
        palabras = ['mouredev','bryanguevara','desarrolloweb','ingeniero']
        return random.choice(palabras)
    
    def cantidadEliminar(self, word):
        longitud = len(word)
        #caractares ente el 1 y 60% de la palabra
        num = int((60 * longitud)/100)
        rando = random.randint(1, num)
        return random.sample(range(len(word)), rando)
    
    def check_word(self, word, word_end, lista, incog):
        lista_word = list(word)
        lista_word_end = list(word_end)
        for i in lista:
            if lista_word[i] == incog:
                lista_word_end[i] = incog
        return "".join(lista_word_end)

    def palabra(self, word, delet):
        lista_word = list(word)
        rando = delet
        for index in rando:
            lista_word[index] = '_'
        return "".join(lista_word)
    
    def star_game(self):
        word = self.palabraRandom()
        list_element = self.cantidadEliminar(word)
        word_end = self.palabra(word, list_element)
        intentos = 5
        print("Juego de Adivinar Palabra")
        
        while intentos > 0:
            print(f"* Tienes {intentos} intentos\n* Tu palabra es: {word_end}")
            word_input = str(input("Ingrese una letra o palabra: "))
            if len(word_input) > 1:
                if word_input == word:
                    print(f"¡WOW Ganaste el juego!... Palabra Correcta: {word}")
                    break
                else:
                    print(f'Palabra incorrecta')
                    intentos -= 1
            else:
                word_end_new = self.check_word(word, word_end, list_element, word_input)
                if word_end_new == word:
                    print(f"¡WOW Ganaste el juego!...Palabra Correcta: {word}")
                    break
                elif word_end != word_end_new:
                    word_end = word_end_new    
                    print(f"Letra Correcta")
                else:
                    print(f"Letra Incorrecta")
                    intentos -= 1

        if intentos == 0:
            print(f"¡Perdiste el juego :(! Te quedaste sin intentos\nLa palabra correcta: {word}")

adivina = adivinarPalabra()
adivina.star_game()
