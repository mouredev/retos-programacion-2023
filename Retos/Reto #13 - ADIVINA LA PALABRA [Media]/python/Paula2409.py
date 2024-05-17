"""
/*
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
 */
 """
import random
def process_word():
    """
    A word guessing game where the player can guess letters or the
    whole word with limited attempts.
    
    Args:
        None
    
    Returns:
        None
    """
    words = ['teclado', 'anteojos','monitor', 'calefactor','edificio','cinturon',
    'boligrafo','habitacion','libros','persona','planeta','televisor','telefono','direccion']

    hidden_letters = []
    new_word_to_guess = word_to_guess = random.choice(words)
    quantity_letters_to_hide = int(len(new_word_to_guess)*0.6)
    list_positions = [quantity_letters for quantity_letters in range(quantity_letters_to_hide)]
    while len(list_positions) != 0:
        letter_to_hide = random.randrange(len(new_word_to_guess))
        if letter_to_hide not in hidden_letters:
            hidden_letters.append(letter_to_hide)
            list_positions.pop()
    for position in hidden_letters:
        new_word_to_guess = new_word_to_guess.replace(new_word_to_guess[position],"_",1)
    return [new_word_to_guess,word_to_guess]

def guess_word():
    new_word_to_guess = process_word()[0]
    word_to_guess = process_word()[1]
    intentos = 5
    while intentos != 0:
        print("""Escriba la opcion:
        1. Adivinar por letra
        2. Adivinar por palabra
        3. Volver a empezar
        4. Salir
        """)
        option = input()
        while option != 4:
            if option == 1:
                guess = input("Escriba la letra: ")
                if guess in word_to_guess:
                    new_word_to_guess.replace("_",guess)
                    print(f"La palabra es: {new_word_to_guess}")
                else:
                    print(f"Lo siento. Esa letra no esta en la palabra. La palabra es: {new_word_to_guess}")
                    intentos -= 1
            elif option == 2:
                guess = input("Escriba la palabra: ")
                if guess == word_to_guess:
                    print(f"Bien! La palabra es: {word_to_guess}")
                else:
                    print(f"Lo siento, esa no es la palabra")
                    intentos -= 1
            elif option == 3:
                guess_word()
            if "_" not in new_word_to_guess:
                print(f"Has adivinado la palabra, es: {new_word_to_guess}")
    
    print(f"No ha podido adivinar la palabra: {word_to_guess}")

print(process_word())
guess_word()