# Reto #13: Adivina la palabra
#### Dificultad: Media | Publicación: 27/03/23 | Corrección: 03/04/23

## Enunciado

#
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
#

import random
import requests


class GuessWord:
    def __init__(self, number_of_attempts):
        self.number_of_attempts = number_of_attempts

    # Obtenemos una palabra
    def obtain_word(self):
        url_query = "https://random-word-api.herokuapp.com/word?lang=es"
        response = requests.get(url_query)
        word_json = response.json()[0]
        return word_json.lower()

    # Calculamos el 60% de la longitud de la palabra
    def len_60_percent(self, word):
        return int((60 * len(word)) / 100)

    # Generamos un numero al azar entre 1 y el 60% para eliminar letras
    def generate_random_number(self, max_number):
        return random.randint(1, max_number)

    # Quitamos al azar letras de palabra basados en el numero al azar entre 1 y el 60%
    def remove_random_characters(self, word):
        num_to_remove = self.generate_random_number(self.len_60_percent(word))
        char_list = list(word)
        index_to_remove = random.sample(range(len(char_list)), num_to_remove)

        for index in sorted(index_to_remove, reverse=True):
            char_list[index] = "_"
        return "".join(char_list)

    # Validamos si encontró la palabra
    def check_win(self, guess_word, initial_word):
        return guess_word == initial_word

    # Jugamos
    def play_game(self):
        word = self.obtain_word()
        removed_word = self.remove_random_characters(word)
        print(removed_word)

        for i in range(self.number_of_attempts):
            user_input = input("Ingresa una letra o una palabra: ")
            if len(user_input) > 1:
                if len(user_input) != len(word):
                    print("La palabra debe tener la misma longitud")
                    continue
                elif self.check_win(user_input, word):
                    print("Adivinaste la palabra!!!")
                    break
                else:
                    print("Esa no es la palabra")
            elif user_input in word:
                for index, char in enumerate(word):
                    if char == user_input:
                        removed_word_list = list(removed_word)
                        removed_word_list[index] = user_input
                        removed_word = "".join(removed_word_list)
                print(removed_word)
                if self.check_win(removed_word, word):
                    print("Adivinaste la palabra!!!")
                    break
            else:
                print("La letra no está en la palabra.")
                print(removed_word)
        else:
            print("Se acabaron los intentos y no adivinaste la palabra")
            print(f"La palabra era: {word}")


if __name__ == "__main__":
    number_of_attempts = int(input("Nro. de intentos?: "))
    game = GuessWord(number_of_attempts)
    game.play_game()
