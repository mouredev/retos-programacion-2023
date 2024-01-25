"""
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
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
 """

import random


def show_random_word (word):
    
    palabra_a_adivinar = ""

    letra_a_remplazar = random.sample(range(len(word)), int(0.6 * len(word)))
    cont = 0   
    for i in range(len(word)):
        if i in letra_a_remplazar:
            palabra_a_adivinar += "_"
            cont += 1                      
        else:
            palabra_a_adivinar += word[i]

    print(f"Tienes {cont} intentos para poder adivinar")
    return list(palabra_a_adivinar)
    

def show_word (palabra_a_adivinar):
    return "".join(palabra_a_adivinar)

def find_word (palabra_a_adivinar, num):

    trys = 0

    while trys < num:
        user_letter = input("Introduce una letra para adivinar: ").lower()

        if len(user_letter) == 1 and user_letter.isalpha():     # Se verifica que la entrada del usuario sea una sola letra y que sea alfabética
            if user_letter in word:
                print("Usted adivino una letra")
                for i, letra in enumerate(word):
                    if letra == user_letter:
                        palabra_a_adivinar[i] = user_letter
                                       
                print(f"La palabra actual es: {palabra_a_adivinar}")

                if "_" not in palabra_a_adivinar:
                    print(f"Felicidades a encontrado la palabra {word}")
                    break
            else:
                print("La letra no esta en la palabra intenta de nuevo")
                trys += 1
            if trys == intentos:
                print("Perdiste no encontraste la palabra oculta")
                break
        
        else:
            print("Entrada no valida ingrese una sola letra")

word_list = ["windows", "tecnologia", "software", "development", "languages", "python", "visual", "program"]    
word = random.choice(word_list)

word_to_guess = show_random_word(word)
print(show_word(word_to_guess))

intentos = int(0.6 * len(word))
find_word(word_to_guess, intentos)




