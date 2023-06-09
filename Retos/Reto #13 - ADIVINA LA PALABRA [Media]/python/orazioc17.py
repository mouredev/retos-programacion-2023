import random
import time


class Game:
    words = ['elefante', 'hipopotamo', 'programacion',
             'javascript', 'teclado', 'escritorio', 'computador']
    lives = 5

    def __init__(self):
        self.chosen_word = random.choice(self.words)
        self.word_to_show, self.percent_removed = self.__prepare_word(
            self.chosen_word)

    @staticmethod
    def __prepare_word(word: str) -> str:
        """
        Function where I prepare the word removing letters and replacing them with the underscore (_)
        With the condition of not removing more than the 60% of the letters
        """
        letter_list = list(set(list(word)))
        while True:

            if len(letter_list) == 0:
                # If the list is already empty, then I return the word with the percentaje
                # Porcentaje ocultado
                return word, (word.count('_') / len(word))

            if '_' in letter_list:
                letter_list.remove('_')

            letter = random.choice(letter_list)

            aux_word = word.replace(letter, '_')

            if (1 - (aux_word.count('_') / len(word))) < 0.4:
                # With this I check that I can remove the letter and stay in the range of max 60% removed
                # If this is True, then I discard this letter and continue with the loop
                letter_list.remove(letter)
                continue
            else:
                # Removing the letter from the word
                word = word.replace(letter, '_')
                letter_list.remove(letter)

    def __get_input(self) -> str:
        while True:
            user_input = input(
                'Type a letter or the entire word (It has to be the same length): ').lower()
            if user_input == 0:
                print('You did not type anything, try again\n')
                continue
            elif len(user_input) == 1 or len(user_input) == len(self.word_to_show):
                return user_input
            else:
                print('Bad input (Different length of the word)')
                continue

    def game_loop(self):
        letter_positions = {}
        for letter in self.chosen_word:
            if letter not in self.word_to_show:
                letter_positions[letter] = [index for index, l in enumerate(
                    self.chosen_word) if self.chosen_word[index] == letter]
        while self.lives > 0:
            if len(letter_positions) == 0:
                print(f'Nice! You have won! The word was {self.chosen_word}')
                exit()
            print()
            print(f'Number of lives: {self.lives}')
            print(f'Word to find: {self.word_to_show}')
            user_input = self.__get_input()
            # self.lives = 0
            if len(user_input) == 1:
                if user_input in letter_positions.keys():
                    for index in letter_positions[user_input]:
                        word_to_show = list(self.word_to_show)
                        word_to_show[index] = user_input
                        self.word_to_show = ''.join(word_to_show)
                    letter_positions.pop(user_input)
                else:
                    if self.lives == 1:
                        print(
                            f'Another bad guess, you ran out of lives, you lost! The word was {self.chosen_word}')
                    print('Bad guess, try again')
                    self.lives -= 1
                    continue
            else:
                if user_input == self.chosen_word:
                    print(
                        f'You guessed, that is the word, you have won! The word was {self.chosen_word}')
                    exit()
                else:
                    if self.lives == 1:
                        print(
                            f'Another bad guess, you ran out of lives, you lost! The word was {self.chosen_word}')
                    print('Bad guess, try again')
                    self.lives -= 1
                    continue

    def __str__(self):
        return f'Word to guess: {self.word_to_show}'


if __name__ == '__main__':
    game = Game()
    game.game_loop()
