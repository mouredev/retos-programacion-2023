import random
import os
import time

def choice_word():
    words = ['capibara', 'marmota', 'crazydev']
    return random.choice(words)

def fade_word(word: str):
    idx_fade = random.choices(range(len(word)), k=int(len(word) * 0.6))
    ocult_word = list(word)
    for i in idx_fade:
        ocult_word[i] = '_'
    return ocult_word, idx_fade

def testing_word(word, user_input, ocult_word, idx):
    if user_input == word:
        return list(word), True
    else:
        for i in idx:
            if word[i] == user_input:
                ocult_word[i] = word[i]

def game():
    word = choice_word()
    ocult_word, idx = fade_word(word)
    intentos = len(word) + 4
    status = False

    while not status and intentos > 0:
        os.system('clear')
        print(f'Intentos restantes: {intentos}\n')
        print(''.join(ocult_word))

        user_input = input('Ingrese una letra o la palabra completa: ').strip()

        if not user_input.isalpha():
            print('⚠️ Ingrese solo letras.')
            time.sleep(1)
            intentos -= 1
            continue

        if len(user_input) > 1 and len(user_input) != len(word):
            print('⚠️ Ingrese una letra o una palabra con la longitud correcta.')
            time.sleep(1)
            intentos -= 1
            continue

        # Validar la entrada del usuario
        if user_input == word:
            ocult_word, status = list(word), True
        elif user_input not in word:
            print('❌ Letra incorrecta.')
            intentos -= 1
            time.sleep(1)
        else:
            ocult_word, status = testing_word(word, user_input, ocult_word, idx)

    os.system('clear')
    if status:
        print(f'🎉 ¡Ganaste! La palabra era: {word}')
    else:
        print(f'❌ ¡Perdiste! La palabra era: {word}')

game()
