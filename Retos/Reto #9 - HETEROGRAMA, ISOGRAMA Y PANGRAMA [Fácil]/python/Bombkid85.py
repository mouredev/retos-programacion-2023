import math

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def heterograma(phrase):
    phrase = phrase.lower()
    for letter in phrase:
        if letter in abc:
            count = 0
            for letter_compare in phrase:
                if letter_compare == letter:
                    count = count + 1
                if count > 1:
                    return "No es un heterograma"
    return "Es un heterograma"

def isograma(phrase):
    phrase = phrase.lower()
    letters_count = set({})
    for letter in phrase:
        if letter in abc:
            count = 0
            for letter_compare in phrase:
                if letter_compare == letter:
                    count = count + 1
            letters_count.add(count)
    if len(letters_count) > 1:
        return "No es un isograma"
    elif max(letters_count) == 1:
        return "No es un isograma"
    else:
        return "Es un isograma"

def pangrama(phrase):
    phrase = phrase.lower()
    letters_list = []
    for letter in phrase:
        if letter in abc and letter not in letters_list:
                    letters_list.append(letter)
    if len(letters_list) == len(abc):
        return "Es un pangrama"
    else:
        return "No es un pangrama"

            
print(heterograma("Hola que haces"))
print(heterograma("Trueno a mil"))
print(isograma("Trueno a mil"))
print(isograma("Hola que haces"))
print(isograma("Bebe"))
print(pangrama("Hola que haces"))
print(pangrama("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú."))