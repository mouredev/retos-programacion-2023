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
import os

def choose_random_word():

    word_list = ["Programación", "Desarrollo", "Terminal", "Computadora",
                "Deportes", "Universidad", "Estudiante", "Ingeniero",
                "Ciencia", "Matemáticas", "Investigación", "Desarrollador",
                "Programador", "Inteligencia", "Aprendizaje",
                "Automático", "Estructura", "Datos", "Algoritmo"]    
    return random.choice(word_list).lower()


def hide_word(word):
    num_hidden = round(len(word) * 0.6)
    hidden_indices = random.sample(range(len(word)), num_hidden)
    hidden_word = ""
    for i, letter in enumerate(word):
        if i in hidden_indices:
            hidden_word += "_"
        else:
            hidden_word += letter
    return hidden_word

def choose_difficulty():

    difficulty = 0

    while difficulty < 1 or difficulty > 3:
        difficulty = int(input("\nElige la dificultad (1, 2 o 3): "))

    return difficulty

def main():

    os.system("cls")

    working_word = choose_random_word()
    word = list(working_word)
    hidden_word = list(hide_word(word))

    print("\n¡Bienvenido a Adivina la Palabra!")
    difficulty = choose_difficulty()
    if difficulty == 1:
        attemps = 10
    elif difficulty == 2:
        attemps = 7
    else:
        attemps = 5
    
    print(f"\nHas elegido la dificultad {difficulty}. Tienes {attemps} intentos.")
    print(f"\nDebes de adivinar la siguiente palabra ---> {' '.join(hidden_word)}")

    while attemps > 0:

        user_input = input("\nIngresa una letra o la palabra completa: ")

        if len(user_input) == 1: #Validar que la elección sea válida
            if user_input in word:
                for char in word:
                    if char == user_input:
                        index = word.index(char)
                        hidden_word[index] = char
                        word[index] = "_" #Para que no se repita la letra
                os.system("cls")
                if "_" not in hidden_word:
                    print(f"\n¡Ganaste! La palabra era {working_word}.")
                    break
                print(f"\n¡Correcto! La letra {user_input} está en la palabra.")
                print(f"\n---> {' '.join(hidden_word)}")
            else:
                os.system("cls")
                attemps -= 1
                print(f"\n¡Incorrecto! La letra {user_input} no está en la palabra.")
                print(f"\n---> {' '.join(hidden_word)}")
        elif len(user_input) == len(word):
            if user_input == working_word.lower():
                print(f"\n¡Correcto! La palabra es {user_input}.")
                break
            else:
                attemps -= 1
                os.system("cls")
                print(f"\n¡Incorrecto! La palabra no es {user_input}.")
                print(f"\n---> {' '.join(hidden_word)}")
        else:
            attemps -= 1
            os.system("cls")
            print("---------------------------------\nDebes de escoger una sola letra o adivinar la palabra.\n---------------------------------")
            print(f"\n---> {' '.join(hidden_word)}")
        print(f"\nTe quedan {attemps} intentos.")
    else:
        print(f"\n¡Perdiste! La palabra era {working_word}.")

main()
