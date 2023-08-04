import random
import urllib.request
import re

def hide_word(word):
    length = len(word)
    hidden_letter = 0
    while hidden_letter < 0.4*length:
        i = random.randint(0, length - 1)
        letter = word[i]
        for j in range(len(word)):
            if letter == word[j]:
                list_word = list(word)
                list_word[j] = "_"
                word = "".join(list_word)
                hidden_letter = word.count("_")
    return word

def find_letter(my_letter, word):
    for i, letter in enumerate(word):
        if letter == my_letter:
            yield i

url = 'https://es.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol'
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
words = re.findall(r"([a-zA-Zá-úÁ-Ú]+)</span>", html, flags=re.DOTALL)
word = random.choice(words).lower()
attempt = 5

hidden_word = hide_word(word)
solved_word = list(hidden_word)
print("ADIVINA LA PALABRA:", hidden_word)

while attempt > 0:
    my_word = input(f"\nIntroduce una letra o resuelve la palabra completa (intentos restantes {str(attempt)}):")
    if len(my_word) == 1:
        if my_word in solved_word:
            print("Esa letra ya se encuentra en la palabra")
        elif my_word in word:
            positions = list(find_letter(my_word, word))
            for i in positions:
                solved_word[i] = my_word
            print(f"Se han encontrado {len(positions)} coincidencias. {''.join(solved_word)}")
        else:
            print("Se han encontrado 0 coincidencias")
    else:
        if my_word == word:
            print("Enhorabuena. Se ha resuelto la palabra")
            break
        else:
            print("No es la palabra correcta")
    if not "_" in solved_word:
            print("Enhorabuena. Se ha resuelto la palabra")
            break
    attempt -= 1
print(f"\nFIN DEL JUEGO\nSolución: {word}")