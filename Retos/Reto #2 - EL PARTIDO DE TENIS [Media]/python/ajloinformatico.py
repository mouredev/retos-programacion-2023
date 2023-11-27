from random import randint
from os import system

"""
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
15 - Love
30 - Love
30 - 15
30 - 30
40 - 30
Deuce
Ventaja P1
Ha ganado el P1
Si quieres, puedes controlar errores en la entrada de datos.   
Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""

APP_NAME = """
#######################################
            TENNIS MATCH

            by infolojo
          https:://infolojo.es
        Antonio José Lojo Ojeda
#######################################
"""
DEUCE = "DEUCE"
ADVENTAGE = "ADVENTAGE"

class Match:
    def __init__(self, playerOne: str = "", playerTwo: str = ""):
        self.playerOne: str = playerOne
        self.playerTwo: str = playerTwo
        self.service: int = 0
        self.playerOnePoint: int = 0
        self.playerTwoPoint: int = 0
        self.pointsList = ["Love", "15", "30", "40", "GAME"]

    def add_players(self):
        if self.playerOne == "":
            self.playerOne = input("Please enter P1 name:\n>> ")
        if self.playerTwo == "":
            self.playerTwo = input("Please enter P2 name:\n>> ")

        return f"\nPlayers {self.playerOne} and {self.playerTwo} are ready"

    def launch_round(self, mockk: bool = False):
        if mockk == True:
            self.playerOnePoint += 1
            self.playerTwoPoint += 1

        else:
            playerWinner: str = [self.playerOne, self.playerTwo][randint(0, 1)]
            if playerWinner == self.playerOne:
                self.playerOnePoint += 1
            elif playerWinner == self.playerTwo:
                self.playerTwoPoint += 1


        actualPoints: str
        if self.playerOnePoint >= 3 and self.playerTwoPoint >= 3:
            # deuce
            if self.playerOnePoint == self.playerTwoPoint:
                actualPoints = f"\n{self.playerOne} - {DEUCE} | {self.playerTwo} - {DEUCE}"
            
            # player one wins
            elif self.playerOnePoint - self.playerTwoPoint == 2:
                actualPoints = f"\n{self.playerOne} - GAME | {self.playerTwo} - 40"

            # player one wins
            elif self.playerTwoPoint - self.playerOnePoint == 2:
                actualPoints = f"\n{self.playerOne} - 40 | {self.playerTwo} - GAME"

            # player one ADVENTAGE
            elif self.playerOnePoint > self.playerTwoPoint:
                actualPoints = f"\n{self.playerOne} - {ADVENTAGE} | {self.playerTwo} - 40"

            elif self.playerTwoPoint > self.playerOnePoint:
                actualPoints = f"\n{self.playerOne} - 40 | {self.playerTwo} - {ADVENTAGE}"

        else:
            actualPoints = f"\n{self.playerOne} - {self.pointsList[self.playerOnePoint]} | {self.playerTwo} - {self.pointsList[self.playerTwoPoint]}"
        
        print(actualPoints)

    def clear_screen(self):
        # uncomment by checking your or
        # clear windows screen
        # system('CLS')
        # clear linux screen
        system('clear')

    def check_winner(self):
        winner: str = ""
        if self.playerOnePoint >= 3 and self.playerTwoPoint >= 3:
            if self.playerOnePoint > 3 and (self.playerOnePoint - self.playerTwoPoint == 2):
                winner = f"\nCongratulations {self.playerOne.upper()} YOU WINS\n"
            elif self.playerTwoPoint > 3 and (self.playerTwoPoint - self.playerOnePoint == 2):
                winner = f"\nCongratulations {self.playerTwo.upper()} YOU WINS\n"
        
        elif self.playerOnePoint == 4:
            winner = f"\nCongratulations {self.playerOne.upper()} YOU WINS\n"
        elif self.playerTwoPoint == 4:
            winner = f"\nCongratulations {self.playerTwo.upper()} YOU WINS\n"

        if winner != "":
            print(winner)
            return True
        return False

    def run(self):
        self.clear_screen()
        print(APP_NAME)
        print(self.add_players())

        while(True):
            # check to finish game
            if self.check_winner():
                return

            # upgrade service number
            self.service += 1
            print(f"\nService number {self.service}:")
            

            # launch rounf game
            self.launch_round()
        
if __name__ == "__main__":
    Match().run()