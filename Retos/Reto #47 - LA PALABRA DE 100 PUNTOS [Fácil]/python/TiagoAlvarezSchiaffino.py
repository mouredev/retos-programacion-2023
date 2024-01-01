def calculate_points(word):
    """
    Calculate the points for a word based on the assigned value for each letter.

    Args:
        word (str): The word for which the points will be calculated.

    Returns:
        int: Total points for the word.
    """
    letter_values = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
        "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "Ñ": 15, "O": 16, "P": 17,
        "Q": 18, "R": 19, "S": 20, "T": 21, "U": 22, "V": 23, "W": 24, "X": 25,
        "Y": 26, "Z": 27,
    }
    total_points = sum(letter_values.get(letter.upper(), 0) for letter in word)
    return total_points


def word_100_points_game():
    """
    Game to accumulate points by forming words.
    The game ends when 100 points or more are reached in a word.
    """
    print('''
    Rules: To win, you must enter a word and the sum of its
    letters should be 100 points. The letter 'A' is worth 1 point and 'Z'
    is worth 27 points. It is case-insensitive. Enjoy the game!
    ''')
    total_points = 0

    while total_points < 100:
        word = input("Enter a word: ")
        word_points = calculate_points(word)

        print(f"Word: {word}, Points for the word: {word_points}")

        if word_points >= 100:
            print("Congratulations! You have reached 100 points.")
            break

        print(f'Total accumulated points: {total_points + word_points}')
        print('Do you want to try again? (Y/N)')
        response = input()[0].upper()

        if response != "Y":
            print("Thanks for participating!")
            break

        total_points += word_points


if __name__ == "__main__":
    word_100_points_game()
