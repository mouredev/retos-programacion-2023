import random

class RamdonWord:
    def __init__(self, attempts=5):
        self.words = ["ordenador","monitor","teclado","archivador","libreta","escritorio","sujetapapeles","carpeta","calculadora","calendario"]
        self.word = self.words[random.randint(0, len(self.words) - 1)]
        self.hidden_word = self._hide_letter_in_game_word()
        self.attempts = attempts

    def _hide_letter_in_game_word(self):
        hidden_word = list(self.word)
        num_to_hide = int(len(self.word) * 0.6)
        indices_to_hide = random.sample(range(len(self.word)), num_to_hide)
    
        for i in indices_to_hide:
            hidden_word[i] = "_"
    
        return "".join(hidden_word)

    def _show_game_word(self):
        print(f"La palabra a adivinar es: {self.hidden_word}")

    def _check_word_in_game_word(self, word):
        if word == self.word:
            return True
        return False

    def _check_letter_in_game_word(self, letter):
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.hidden_word = self.hidden_word[:i] + letter + self.hidden_word[i + 1:]
            return True
        return False

    def play(self):
        while self.attempts > 0:
            self._show_game_word()
            user_input = input("Introduce una letra o la palabra a adivinar: ")
            if len(user_input) == 1:
                if self._check_letter_in_game_word(user_input):
                    if self.hidden_word == self.word:
                        print("¡Has adivinado la palabra!")
                        break
                else:
                    self.attempts -= 1
                    
            elif len(user_input) == len(self.word):
                if self._check_word_in_game_word(user_input):
                    print("¡Has adivinado la palabra!")
                    break
                else:
                    print("La palabra introducida no es correcta")
                    self.attempts -= 1
            else:
                if len(user_input) > 1:
                    print("La longitud de la palabra introducida no es correcta")
                    self.attempts -= 1

            print(f"Te quedan {self.attempts} intentos")

        if self.attempts == 0:
            print(f"Has perdido. La palabra era {self.word}")

if __name__ == "__main__":
    random_word = RamdonWord()
    random_word.play()        
