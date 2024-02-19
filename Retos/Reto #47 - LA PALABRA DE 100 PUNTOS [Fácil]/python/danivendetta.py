# /*
#  * La última semana de 2021 comenzamos la actividad de retos de programación,
#  * con la intención de resolver un ejercicio cada semana para mejorar
#  * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
#  *
#  * Crea un programa que calcule los puntos de una palabra.
#  * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
#  *   español de 27 letras, la A vale 1 y la Z 27.
#  * - El programa muestra el valor de los puntos de cada palabra introducida.
#  * - El programa finaliza si logras introducir una palabra de 100 puntos.
#  * - Puedes usar la terminal para interactuar con el usuario y solicitarle
#  *   cada palabra.
#  */
# ```
import string
import getpass as gt
def create_dict_abc_values(abc: list) -> dict:
    val = 1
    abc_values_reference = dict()
    for char in abc:
        abc_values_reference.update({char: val})
        val += 1
    return abc_values_reference

def calculate_word_value(word: str, abc_values_reference: dict) -> int:
    value = 0
    for char in word:
        try:
            value += abc_values_reference[char]
        except Exception as Error:
            print(f"Tu diccionario no contiene la letra {Error} por lo tanto, te sumará 0 puntos")
            print(Error)
        # print(f'{char} vale {abc_values_reference[char]}')

    return value

def select_diccionario() -> list:
    diccionario = None
    while not diccionario:
        diccionario = input("Elige que diccionario usar: EN or ES:\n").upper()
        if diccionario == "ES":
            abc = list(string.ascii_lowercase)
            abc.insert(14, "ñ")
        elif diccionario == "EN":
            abc = list(string.ascii_lowercase)
        else:
            diccionario = None

    return abc

def select_word() -> str:
    word = input("Escribe tu palabra!:\n").lower()
    while not word.isalpha():
        word = input("Escribe tu palabra! sin numeros ni simbolos!!:\n").lower()

    return word
def start_game():
    user = gt.getuser().title()
    print(f'{user} bienvenido a "La palabra mágica de 100 puntos"')
    jugando = True
    abc = select_diccionario()
    abc_ref_values = create_dict_abc_values(abc)
    while jugando:
        word = select_word()
        word_value = calculate_word_value(word, abc_ref_values)
        print(f'Palabra: {word} vale: {word_value} puntos.\n')
        if word_value == 100:
            print(f'Tenemos palabra ganadora: {word}:\n')
            seguir = input(f'{user} ¿quieres seguir jugando? [y/N]:\n').lower()
            if seguir == "y":
                continue
            else:
                jugando = False


    print(f'Gracias {user} por jugar y hasta la proxima')


if __name__ == "__main__":
    # abc = list(string.ascii_lowercase)
    # abc_es = abc.copy()
    # abc_es.insert(14, "ñ")
    # abc_values_reference = create_dict_abc_values(abc_es)
    # word1 = "murcielago"
    # word2 = "ñapa"
    # calculate_word_value(word1, abc_values_reference)
    # calculate_word_value(word2, abc_values_reference)

    start_game()