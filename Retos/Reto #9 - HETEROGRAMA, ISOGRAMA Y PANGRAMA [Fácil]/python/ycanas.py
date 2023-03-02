from string import ascii_lowercase
import re


def only_letters(phrase):
    return re.sub(r"[^a-z]", '', phrase)

# Alternativa -> set(phrase) [Genera un conjunto "set" (No admite valores repetidos)]
def is_heterogram(phrase):
    phrase = only_letters(phrase)
    stack = []

    for letter in phrase:
        if letter in stack:
            return False
        
        stack.append(letter)

    return True


def is_isogram(phrase):
    phrase = only_letters(phrase)
    stack = {}

    for letter in phrase:
        if letter in stack:
            stack[letter] += 1
        
        else:
            stack[letter] = 1

    occurrences = list(stack.values())

    for i in range(len(occurrences)-1):
        if not occurrences[i] == occurrences[i+1]:
            return False

    return True


def is_pangram(phrase):
    return True if all(letter in only_letters(phrase) for letter in ascii_lowercase) else False


print(is_heterogram("hello world"), is_heterogram("helo wrd"))
print(is_isogram("oso"), is_isogram("osos"))
print(is_pangram("abcdefghijklmnopstuv"), is_pangram("abcdefghijklmnopqrstuvwxyz"))
