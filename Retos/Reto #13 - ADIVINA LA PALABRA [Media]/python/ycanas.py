from random import choice, sample

class Game():
    def __init__(self):
        self.WORDS = ["estructurada", "objetos", "funcional", "reactiva", "imperativa", "declarativa"]
        self.LIVES = 3
        self.DIFFICULTY = 60

        self.word = choice(self.WORDS)
        self.game = list(self.word)
        self.letters = set()

        self.LENGTH = len(self.word)

    
    def won(self):
        print(f"\nGenial... Adivinaste. La palabra es: {self.word}")


    def success(self):
        print("\nMuy bien... Acertaste!")


    def failure(self):
        print("\nQue mal... No acertaste!")


    def validate_letter(self, user_input):
        return user_input in self.letters
    

    def validate_word(self, user_input):
        return user_input == self.word or self.word == "".join(self.game)


    def display(self, attempts):
        word = " ".join(self.game)
        print(f"Palabra: {word} \nIntentos: {attempts+1}\n")


    def transform(self):
        n_letters  = (self.LENGTH * self.DIFFICULTY) // 100
        indexs = sample(range(self.LENGTH), n_letters)

        for index in indexs:
            self.letters.add(self.game[index])
            self.game[index] = '_'
    

    def fill_word(self, user_input):
        self.letters.remove(user_input)

        for index, letter in enumerate(self.word):
            if letter == user_input:
                self.game[index] = user_input


    def play(self):
        self.transform()
        attempts = self.LIVES - 1 

        while attempts in range(self.LIVES):
            self.display(attempts)
            user_input = input("Ingrese una letra o la palabra: ")

            if len(user_input) == self.LENGTH:
                if self.validate_word(user_input):
                    self.won()
                    break

                else:
                    self.failure()
                    attempts -= 1

            elif len(user_input) == 1:
                if self.validate_letter(user_input):
                    self.fill_word(user_input)

                    if self.validate_word(user_input):
                        self.won()
                        break

                    self.success()

                else:
                    self.failure()
                    attempts -= 1

            else:
                print("\nEntrada no valida, vuelve a intentarlo !")


game = Game()
game.play()
