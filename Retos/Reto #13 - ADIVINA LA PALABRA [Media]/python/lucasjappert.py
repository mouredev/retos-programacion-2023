import random

MAX_TRIES = 5
POSIBLE_WORDS = ["hola", "mundo", "python", "javascript", "programacion", "computadora", "teclado", "raton", "monitor", "escritorio", "silla", "mesa", "lampara", "ventana", "puerta", "pared", "piso", "techo", "casa", "edificio", "ciudad", "pais", "continente", "planeta", "sistema", "galaxia", "universo", "vida", "muerte", "nacimiento", "crecimiento", "desarrollo", "evolucion", "revolucion", "independencia", "libertad", "igualdad", "fraternidad", "solidaridad", "amor", "odio", "paz", "guerra", "violencia", "delincuencia", "corrupcion", "impunidad", "justicia", "ley", "derecho", "obligacion", "deber", "moral", "etica", "valores", "principios", "virtudes", "vicios"]

def get_random_word():
    return random.choice(POSIBLE_WORDS)

def get_initial_hidden_word(word: str, percentage_to_hide: float = 0.6):
    number_of_letters_to_hide = int(len(word) * percentage_to_hide)
    indexes_to_hide = random.sample(range(len(word)), number_of_letters_to_hide)
    current_list_of_words = list(word)
    for i in indexes_to_hide:
        current_list_of_words[i] = "_"
    return current_list_of_words

def get_joined_list(list: list[str]):
    return "".join(list)

def start_game():
    current_tries = 1
    print("Bienvenido a Adivina la palabra")
    print("Tienes 5 intentos para adivinarla. Buena suerte!")
    print("")

    WORD_TO_GUESS = get_random_word()
    current_list_of_words = get_initial_hidden_word(WORD_TO_GUESS)

    def check_match(): return get_joined_list(current_list_of_words) == WORD_TO_GUESS
    
    while current_tries <= MAX_TRIES:
        print(get_joined_list(current_list_of_words))
        my_input = ""
        while my_input == "":
            my_input = input(f"Ingresa una letra o palabra (intento {current_tries}): ")
            
        if my_input == WORD_TO_GUESS:
            current_list_of_words = list(WORD_TO_GUESS)
            return print(f"Felicidades, ganaste! La palabra era {WORD_TO_GUESS}")
            
        if my_input not in WORD_TO_GUESS:
            print(f"La letra '{my_input}' no esta en la palabra")
            current_tries += 1
            continue
        
        for i in range(len(WORD_TO_GUESS)):
            if WORD_TO_GUESS[i] == my_input:
                current_list_of_words[i] = my_input
                
        if check_match():
            return print(f"Felicidades, ganaste! La palabra era {WORD_TO_GUESS}")

    print(f"Lo siento, perdiste! La palabra era {WORD_TO_GUESS}")

start_game()