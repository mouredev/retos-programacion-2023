alphabet = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "Ñ": 15,
    "O": 16,
    "P": 17,
    "Q": 18,
    "R": 19,
    "S": 20,
    "T": 21,
    "U": 22,
    "V": 23,
    "W": 24,
    "X": 25,
    "Y": 26,
    "Z": 27,
}

TARGET_SCORE = 100


def start():
    score = 0

    while True:
        try:
            word = input("Enter a word: ").strip()
            for letter in [*word]:
                score += alphabet.get(letter.upper())

            if score >= TARGET_SCORE:
                print(f"You won! Your score: {score}")
                break

            print(f"Try again. Score: {score}")

        except TypeError:
            print("Only letters are accepted")


if __name__ == "__main__":
    start()
