import string


class LetterError(Exception):
    def __init__(
        self,
        character,
        message=f"You can only type 1 word of alphabetic characters.",
    ):
        self.character = character
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.character} -> {self.message}"


def generate_points_table() -> dict:
    points = {}
    for letter in zip(list(string.ascii_lowercase), list(range(1, 28))):
        if letter[1] >= 15:
            points[letter[0]] = letter[1] + 1
        else:
            points[letter[0]] = letter[1]
    points["ñ"] = 15
    return points


points_table = generate_points_table()


def deal_with_accent(accent: str) -> str:
    match accent:
        case "á":
            letter = "a"
        case "é":
            letter = "e"
        case "í":
            letter = "i"
        case "ó":
            letter = "o"
        case "ú":
            letter = "u"
    return letter


def score_word(word: str, points: dict) -> int:
    score = 0
    list_letter = list(string.ascii_lowercase)
    list_letter.append("ñ")
    for letter in word.lower():
        if letter in ["á", "é", "í", "ó", "ú"]:
            letter = deal_with_accent(letter)
        if letter not in list_letter:
            raise LetterError(character=letter)
        print(f"{letter} -> {points[letter]}")
        score += points[letter]
    return score


def main():
    score = 0
    while score != 100:
        word = input("Write a word: ")
        score = score_word(word, points_table)

        if score != 100:
            print(f"You have written a word with a score of {score}, try again")
        else:
            print(
                f"You have written a word with a score of {score}. The program will end."
            )


if __name__ == "__main__":
    main()


# Prueba con una de estas: "tritón , atrapados"
