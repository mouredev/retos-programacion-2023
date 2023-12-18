LETTER_VALUES = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "ñ": 15,
    "o": 16,
    "p": 17,
    "q": 18,
    "r": 19,
    "s": 20,
    "t": 21,
    "u": 22,
    "v": 23,
    "w": 24,
    "x": 25,
    "y": 26,
    "z": 27,
}


TARGET_VALUE = 100


def main():
    """
    Ask for words, and return their value, computed as the sum of the values of their letters.
    Any uppercase letter will be converted to lowercase, and any letter not in the
    LETTER_VALUES dictionary will be omitted (given a zero value).

    The program exits when:
    - the value of the word is 100, OR
    - the user introduces no word, OR
    - the user executes a keyboard interrupt
    """
    while True:
        try:
            word = input("Introduce a word (Ctrl+C or introduce no word to exit): ")
        except KeyboardInterrupt:
            return

        if not word:
            return

        value = sum([LETTER_VALUES.get(c, 0) for c in word.lower()])

        print(f"The value of the word '{word}' was {value} points")
        if value == TARGET_VALUE:
            print(f"Since the value was {TARGET_VALUE}, we exit.")
            return


if __name__ == "__main__":
    main()
