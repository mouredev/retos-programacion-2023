from string import ascii_lowercase
from os import system
from time import sleep

""" 
Crea un programa que calcule los puntos de una palabra.
Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
español de 27 letras, la A vale 1 y la Z 27.
El programa muestra el valor de los puntos de cada palabra introducida.
El programa finaliza si logras introducir una palabra de 100 puntos.
Puedes usar la terminal para interactuar con el usuario y solicitarle
cada palabra.
"""

APP_NAME = """
#######################################
             Words Game

            by infolojo
          https:://infolojo.es
        Antonio José Lojo Ojeda
#######################################
"""

class ErrorManager():
    def __init__(self):
        self.base_error: str = "\nError "
        self.empty_error: str = "Your word can not be empty.\n"
        self.blank_spaces_error: str = f"blank sapce are not valid.\n"
        self.invalid_char_error: str = f" is not inside valid words:\n\nVALID WORDS -> " + " ".join(list(ascii_lowercase)) + ".\n"

    def throw_empty_error(self):
        print(f"{self.base_error}{self.empty_error}")

    def throw_blank_spaces_error(self):
        print(f"{self.base_error}{self.blank_spaces_error}")
    
    def throw_invalid_char_error(self, invalid_char: str):
        print(f"{self.base_error}{invalid_char}{self.invalid_char_error}")

class WordsGame():
    def __init__(self):
        self.points: dict = {}
        self.original_player_word: str
        self.error_manager: ErrorManager = ErrorManager()
        self.prepare_points()

    def prepare_points(self):
        i = 1
        self.initial_list: list = []
        for character in ascii_lowercase:
            self.initial_list.append((character, i))
            i += 1
        self.points = dict(self.initial_list)
    
    def clear_screen(self):
        # uncomment by checking your or
        # clear windows screen
        # os.system('CLS')
        # clear linux screen
        system('clear')


    def check_input(self, player_word: str = ""):
        print(player_word)
        if player_word == "":
            self.error_manager.throw_empty_error()
            return False
        for char in list(player_word):
            if char == " ":
                self.error_manager.throw_blank_spaces_error() 
                return False
            elif char not in ascii_lowercase:
                self.error_manager.throw_invalid_char_error(invalid_char = char) 
                return False
        
        return True

    def check_winner(self, player_word: str):
        result = ""
        points = 0
        print(f"\nWe are calculating {self.original_player_word} points ...")
        
        for char in list(player_word):
            result += f"{char} - {self.points[char]} points\n"            
            points += self.points[char]
        
        print(result)
        if (points == 100):
            print("Congratulations YOU WINS !!\n")
        else:
            print(f"Sorry. {player_word} has only {points} points\n")

    def run(self):
        self.clear_screen()
        print(APP_NAME)
        player_word = input("\nPlease input your word\n>>> ")
        self.original_player_word = player_word
        if self.check_input(player_word = player_word.lower()):
            self.check_winner(player_word = player_word.lower())


if __name__ == "__main__":
    WordsGame().run()
    