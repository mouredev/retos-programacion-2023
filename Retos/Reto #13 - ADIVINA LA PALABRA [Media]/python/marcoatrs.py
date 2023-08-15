import random
import sys

secrets = [
    "secreta",
    "palabra",
    "programacion",
    "intentos",
    "dificultad",
    "armonia",
    "comadreja",
    "tomarnos",
    "vibracion",
    "siuuuuuuuuu",
    "oficial",
]


def init(word: str) -> str:
    hidden_chars = int(len(word) * 0.6)
    hidden_word = list(word)
    count = 0
    while count < hidden_chars:
        idx = random.randint(0, len(word) - 1)
        if hidden_word[idx] == "_":
            continue
        hidden_word[idx] = "_"
        count += 1
    return "".join(hidden_word)


def indexes(word: list, input: str) -> list:
    return [(idx, w) for idx, w in enumerate(word) if input == w]


def game(word: str, tries: int = 3):
    hidden_word = init(word)

    while tries > 0:
        print(f"Adivina la palabra: Tienes {tries} intentos")
        print(hidden_word)
        play = input()
        if len(word) == len(play):
            if word == play:
                print("Ganaste")
                sys.exit(0)
            print("Error")
            tries -= 1
            continue
        if len(play) != 1:
            print("La palabra debe ser del mismo tamaño")
            tries -= 1
            continue
        if not play in word:
            print("Error")
            tries -= 1
            continue
        idx = indexes(list(word), play)
        new_hidden_word = list(hidden_word)
        for i, w in idx:
            new_hidden_word[i] = w
        hidden_word = "".join(new_hidden_word)
        if word == hidden_word:
            print(f"Ganaste: {word}")
            sys.exit(0)
    print(f"Perdiste, era {word}")


game(random.choice(secrets))
