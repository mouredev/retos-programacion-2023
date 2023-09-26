"""
    Reto #13: Adivina la palabra
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
from requests_html import HTMLSession
import random

# Turnos de juego
difficulty = {
    "easy": 10,
    "normal": 5,
    "hard": 3
}

LINE = "*" * 70


# Función que captura una palabra aleatorio de una web y retorna la misma.
def catch_a_word():
    word_page = HTMLSession().get("https://www.palabrasaleatorias.com/?fs=1&fs2=0&Submit=Nueva+palabra#")
    return word_page.html.find("tr", first=True).find("div", first=True).text.lower()


def make_game_elements(base_word):
    long_word = len(base_word)
    list_index_word = list(range(long_word))
    result_word = list(base_word)
    letter_of_the_word = []
    for i in range(int(long_word * 0.6)):
        index = random.choice(list_index_word)
        list_index_word.remove(index)
        letter_of_the_word.append(result_word[index])
        result_word[index] = "_"
    return base_word, "".join(result_word), letter_of_the_word, long_word


def game(turns):
    word, hidden_word, list_letters, long_word = make_game_elements(catch_a_word())
    # Main loop
    while turns > 0:
        print(f"Palabra: {hidden_word} \nLongitud: {long_word}\nTURNOS RESTANTES {turns} \n" + LINE)
        user_input = input("Inserta una letra o la palabra a adivinar: ")
        # Control de entrada
        while len(user_input) > 1 and len(user_input) != long_word:
            print("\nENTRADA INVALIDA\n" + LINE)
            user_input = input("Inserta una letra o la palabra a adivinar: ")

        # Descubre la palabra
        if user_input == word:
            print(f"\n¡¡¡HAS GANADO!!!\n Palabra:{word}")
            break

        # Descubre una letra
        elif user_input in list_letters:
            print("\nLETRA DESCUBIERTA")
            hidden_word = list(hidden_word)
            count = 0
            for letter in word:
                if letter == user_input:
                    hidden_word[count] = user_input
                count += 1
            hidden_word = "".join(hidden_word)
            if word == hidden_word:
                print(f"\n¡¡¡HAS GANADO!!!\n Palabra:{word}")
                break

        # No descubre ni la palabra ni una letra
        else:
            print("\nHAS FALLADO")
            turns -= 1

    if turns == 0:
        print(f"\nSE TERMINARON LOS TURNOS\n Palabra: {word}")


if __name__ == "__main__":
    game(difficulty["normal"])
