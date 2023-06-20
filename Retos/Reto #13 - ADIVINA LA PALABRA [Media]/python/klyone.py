#!/usr/bin/env python3

import random

class Game:
    def __init__(self, words = None, try_times=10, min_limit_hidden = 30, max_limit_hidden=60):
        self.try_times = try_times
        self.max_limit_hidden = max_limit_hidden
        self.min_limit_hidden = min_limit_hidden
        if words == None:
            self.words = [
                "murcielago",
                "dinosaurio",
                "apocalipsis",
                "universo",
                "maravilloso",
                "extraordinario",
                "fantastico"
            ]
        else:
            self.words = words
        self.selected_word = ""
        self.hidden_letters = []

    def __hide_letters(self, word):
        num_letters = len(word)
        percentage_to_hidden = random.randint(self.min_limit_hidden, self.max_limit_hidden)
        max_letters_to_hide = int((num_letters * percentage_to_hidden)/100)
        letters_index = list(range(0, num_letters))

        for i in range(max_letters_to_hide):
            pos = random.choice(letters_index)
            self.hidden_letters.append(pos)
            word = list(word)
            word[pos] = "_"
            word = "".join(word)
            letters_index.remove(pos)
        self.hidden_letters.sort()

        return word

    def __select_word(self):
        selected = random.choice(self.words)
        self.selected_word = selected
        selected = self.__hide_letters(selected)
        return selected

    def play(self):
        win = False
        word = self.__select_word()

        print("The word is " + word)
        print("Total try times is " + str(self.try_times))

        while not win and self.try_times > 0:
            l = input("Write the next letter or the whole word: ")
            if len(l) == 1:
               expected_letter = self.selected_word[self.hidden_letters[0]]
               if l == expected_letter:
                   self.hidden_letters.pop(0)
                   word = word.replace("_", l, 1)
                   if (self.hidden_letters == []):
                       win = True
               else:
                   self.try_times = self.try_times - 1
                   print("Wrong: Remaining try times "+str(self.try_times))
            else:
                if len(l) == len(self.selected_word):
                    if l == self.selected_word:
                        word = l
                        win = True
                    else:
                        self.try_times = self.try_times - 1
                        print("Wrong: Remaining try times "+str(self.try_times))
                else:
                    self.try_times = self.try_times - 1
                    print("Wrong: Remaining try times "+str(self.try_times))

            print("Word status: " + word)

        if not win:
            print("You lose, the correct word is " + self.selected_word)
        else:
            print("Congratulations! You win!")


if __name__ == "__main__":
    game = Game()
    game.play()
