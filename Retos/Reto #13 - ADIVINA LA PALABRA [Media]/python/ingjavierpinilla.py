import random


class Game:
    def __init__(self, word: str, attempts: int = 5):
        self.word = word.lower()
        self.attempts = attempts
        self.hidden_characters, self.gameword = self.prepare_word()
        self.running = True
        self.print_current_status()

    def get_index_list_to_hide(self) -> list:
        number_of_characters_to_hide: int = len(self.word) * 60 // 100
        return random.sample(range(0, len(self.word)), number_of_characters_to_hide)

    def prepare_word(self) -> tuple:
        index_list_to_hide: list = self.get_index_list_to_hide()
        gameword: str = self.word
        hidden_characters: dict = {}

        for i in index_list_to_hide:
            if hidden_characters.get(gameword[i]):
                hidden_characters[gameword[i]].append(i)
            else:
                hidden_characters[gameword[i]] = [i]
            gameword = self.replace_character(gameword, i, "_")

        return hidden_characters, gameword

    @staticmethod
    def replace_character(word: str, index: int, new_character: str) -> str:
        return word[:index] + new_character + word[index + 1 :]

    def test_character(self, character_to_test: str) -> int or bool:
        if index_list := self.hidden_characters.get(character_to_test):
            return index_list.pop()
        return False

    def attempt(self, text_to_test: str) -> None:
        if text_to_test == self.word:
            self.gameword = text_to_test
        elif (index := self.test_character(text_to_test)) is not False:
            self.gameword = self.replace_character(self.gameword, index, text_to_test)
        else:
            print(f"{text_to_test} no se encuentra en la palabra misteriosa")
            self.attempts -= 1
        self.check_end()

    def check_end(self) -> None:
        if self.attempts <= 0:
            self.trigger_end(False)
        elif self.word == self.gameword:
            self.trigger_end(True)
        else:
            self.print_current_status()

    def print_current_status(self) -> None:
        print("*" * 40)
        print(f"Attempts: {self.attempts}")
        print(f"Word: {self.gameword}")

    def trigger_end(self, win: bool) -> None:
        self.print_current_status()
        text = "ganado" if win else "perdido"
        print(f"Usted ha {text}")
        self.running = False


if __name__ == "__main__":
    game = Game("avioneta", 5)
    while game.running:
        new_char = input().lower()
        game.attempt(new_char)
