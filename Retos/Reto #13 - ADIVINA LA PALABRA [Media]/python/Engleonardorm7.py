# /*
# * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  *   la palabra a adivinar)
#  *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  *   - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
#  *   ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
#  */

import random
import os


words = ['murderer', 'cemetery', 'translator', 'videogame', 'detective', 'generator']

word = random.choice(words)
number=random.randint(3,len(word)-3)

hidden_indices = random.sample(range(len(word)), number)

hidden_word = ''
for i in range(len(word)):
    if i in hidden_indices:
        hidden_word += '_'
    else:
        hidden_word += word[i]

hidden_word_list=list(hidden_word)
lives=5
guessed_letters=set()
while "_" in hidden_word_list and lives >0:
    
    hidden_word="".join(hidden_word_list)

    print(hidden_word)
    print(f"\nWord: {hidden_word}")
    print(f"Lives left: {lives}")
    print(f"Letters guessed: {hidden_word}")

    guess = input("Guess a letter or the entire word: ").lower()
    os.system("cls")
    if len(guess) == 1:
        
        if  guess in word:
            print("Correct guess!")
            for i in range(0,len(word)):
                if word[i] == guess:
                    hidden_word_list[i]=guess

        else:
            print("Wrong guess!")
           
            lives -= 1
    elif len(guess) == len(word):
        
        if guess == word:
            print("Congratulations, you guessed the word!")
            break
        else:
            print("Wrong guess!")
            lives -= 1
    else:
        print("Invalid guess, please try again.")
        
    if "_" not in hidden_word_list:
        print(f"Congratulations, you guessed the word!: {word}")

    if lives == 0:
        print("Game Over")
            