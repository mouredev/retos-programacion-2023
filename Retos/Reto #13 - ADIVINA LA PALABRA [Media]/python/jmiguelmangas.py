"""* Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */"""

import random

animales = [
    "Gorila", "Chimpancé", "Caballo", "Ballena", "Perro", "Gato", "León", "Tigre", "Elefante",
    "Jirafa", "Delfín", "Camello", "León marino", "Hipopótamo", "Oso", "Ornitorrinco",
    "Zorro", "Rinoceronte", "Guepardo", "Ratón", "Hiena", "Topo", "Jaguar"
    ]
cosas = [
    "armario","balcón", "baño", "comedor", "habitación", "despacho", "dormitorio", "espejo",
    "fregadero", "horno", "horno microondas", "jardín", "lavabo", "lavadero", "lavaplatos",
    "pasillo", "patio", "salón", "sótano", "techo", "bañera", "cama", "cocina", "cocina" ,
    "escalera" ,"lavadora" , "mesa" , "nevera", "puerta", "silla", "terraza", "ventana"
    ]
lista = [animales,cosas]
def get_word():
    select = random.choice(lista)
    return random.choice(select).capitalize()

def camouflage_word(word):
    camu = len(word)* "_"
    new_word = ""
    for i in range(len(word)):
        new_word = new_word + random.choice([camu[i],word[i]])
    return new_word   

def game (guess_word,secret_word):
    lifes = 5
    secret_word_list = list(secret_word)
    guess_word_list = list(guess_word)
    while lifes > 0:
        for character in guess_word_list:
            print(f"{character}",end=" ")
        print("\n")
        attempt = input (f"Vidas Restantes: {lifes} Adivina la Palabra: ")
        print("\n")
        attempt_word_list = list(attempt)
        if attempt == secret_word or guess_word_list == secret_word_list :
            print(f"HAS GANADO has adivinado la palabra {secret_word.upper()}!")
            break
        else:
            if len(attempt_word_list) == len(guess_word_list):
                for i in range(len(secret_word_list)):
                    if attempt_word_list[i] == secret_word_list[i]:
                        guess_word_list[i] = attempt_word_list[i]
                lifes -= 1
            elif len(attempt_word_list) == 1:
                acierto = False
                for i in range(len(secret_word_list)):
                    if attempt_word_list[0] == secret_word_list[i]:
                        guess_word_list[i] = attempt_word_list[0] 
                        acierto = True
                if acierto == False:
                    lifes -= 1
            
            else:
                print("Te has equivocado de longitud de la palabra")
                lifes -= 1
    if lifes == 0:
        print(f"Has perdido, te has quedado sin vidas, la palabra era: {secret_word}")
        
def main():
    secret_word = get_word().lower()
    guess_word = camouflage_word(secret_word).lower()
    game(guess_word,secret_word)
main()