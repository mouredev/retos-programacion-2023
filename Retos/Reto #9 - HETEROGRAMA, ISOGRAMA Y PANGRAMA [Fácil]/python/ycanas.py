from string import ascii_lowercase
import re


def only_letters(phrase):
    return re.sub(r"[^a-z]", '', phrase.lower())


def is_heterogram(phrase):
    phrase = only_letters(phrase)
    letters = set(phrase)

    return len(phrase) == len(letters)


def is_isogram(phrase):
    phrase = only_letters(phrase)
    stack = {}

    for letter in phrase:
        if letter in stack:
            stack[letter] += 1
        
        else:
            stack[letter] = 1

    return len(set(stack.values())) == 1


def is_pangram(phrase):
    return all(letter in only_letters(phrase) for letter in ascii_lowercase)


print(is_heterogram("hello world"), is_heterogram("helo wrd"))
print(is_isogram("amarillo"), is_isogram("Amarillo mrio"))
print(is_pangram("abcdefghijklmnopstuv"), is_pangram("abcdefghijklmnopqrstuvwxyz"))
