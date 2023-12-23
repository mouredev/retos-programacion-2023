import random

def choose_random_word():
    """
    Choose a random word from a predefined list.

    Returns:
        str: A randomly chosen word.
    """
    word_list = ["MoureDev", "Moure", "BraisMoure", "Dev", "BraisMoureDev"]
    return random.choice(word_list)

def hide_word(word):
    """
    Hide a random portion of the word.

    Args:
        word (str): The word to hide.

    Returns:
        str: The word with a portion hidden.
    """
    num_hidden = round(len(word) * 0.6)
    hidden_indices = random.sample(range(len(word)), num_hidden)
    hidden_word = ""
    for i, letter in enumerate(word):
        if i in hidden_indices:
            hidden_word += "_"
        else:
            hidden_word += letter
    return hidden_word

def choose_difficulty():
    """
    Choose the difficulty level.

    Returns:
        int: The chosen difficulty level.
    """
    difficulty = 0
    while difficulty < 1 or difficulty > 3:
        difficulty = int(input("\nChoose the difficulty (1, 2, or 3): "))
    return difficulty

def main():
    """
    Main function to play the word guessing game.
    """
    working_word = choose_random_word()
    word = list(working_word)
    hidden_word = list(hide_word(word))

    print("\nWelcome to Guess the Word!")
    difficulty = choose_difficulty()

    if difficulty == 1:
        attempts = 10
    elif difficulty == 2:
        attempts = 7
    else:
        attempts = 5

    print(f"\nYou chose difficulty {difficulty}. You have {attempts} attempts.")
    print(f"\nYou need to guess the following word ---> {' '.join(hidden_word)}")

    while attempts > 0:
        user_input = input("\nEnter a letter or the complete word: ")

        if len(user_input) == 1:
            if user_input in word:
                for char in word:
                    if char == user_input:
                        index = word.index(char)
                        hidden_word[index] = char
                        word[index] = "_"
                if "_" not in hidden_word:
                    print(f"\nYou won! The word was {working_word}")
                    break
                print(f"\nCorrect! The letter {user_input} is in the word.")
                print(f"\n---> {' '.join(hidden_word)}")
            else:
                attempts -= 1
                print(f"\nIncorrect! The letter {user_input} is not in the word.")
                print(f"\n---> {' '.join(hidden_word)}")
        elif len(user_input) == len(word):
            if user_input == working_word:
                print(f"\nCorrect! The word is {user_input}.")
                break
            else:
                attempts -= 1
                print(f"\nIncorrect! The word is not {user_input}.")
                print(f"\n---> {' '.join(hidden_word)}")
        else:
            attempts -= 1
            print("---------------------------------\nYou must choose a single letter or guess the whole word.\n---------------------------------")
            print(f"\n---> {' '.join(hidden_word)}")
        print(f"\nYou have {attempts} attempts remaining.")

    if attempts == 0:
        print(f"\nYou lost! The word was {working_word}.")

if __name__ == "__main__":
    main()
