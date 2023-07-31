import random

words = ["albert", "elefante"]
word = random.choice(words)
intentos = 8

num_hidden = int(len(word) * 0.5)
positions = random.sample(range(len(word)), num_hidden)

game_word = ""
for i in range(len(word)):
    game_word += word[i] if i not in positions else "_"

print(game_word)

while intentos > 0:
    entrada = input("Escribe una letra o la solución: ")
    if len(entrada) == 1:
        success = False
        if entrada in word:
            for i, letter in enumerate(word):
                if letter == entrada and game_word[i] == "_":
                    game_word = game_word[:i] + entrada + game_word[i + 1:]
                    success = True
            print(game_word)
        if not success:
            print("Incorrecto")
            intentos -= 1
    else:
        if entrada == word:
            print("Has ganado")
            break
        else:
            print("La palabra no es correcta")
            intentos -= 1