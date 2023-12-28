


class Player():
    def __init__(self, initPoints:int):
        self.points = initPoints
    def addPoint(self):
        self.points += 15 if self.points < 30 else 10
    def getPoints(self):
        return self.points
    def __str__(self) -> str:
        return "Love" if self.points == 0 else str(self.points)

class TennisMatch():
    def __init__(self) -> None:
        self.p1 = Player(0)
        self.p2 = Player(0)
        self.stage = 0 # stage=0 <=> points in [0-30]. stage=1 <=> someone points=40. stage2 <=> someone points>40. stage3 <=> finished
        self.advantage = 0 # 0 <=> no advantage. 1 <=> advantage p1. 2 <=> advantage p2
        
    def p1WinsPoint(self):
        if self.stage == 0:
            self.p1.addPoint()
            if self.p1.getPoints() == 40:
                self.stage = 1
        else:
            if self.stage == 1:
                if self.p1.getPoints() == 40:
                    if self.p2.getPoints() < 40:
                        print("Player 1 wins the game!")
                        self.stage = 3 # finished
                    else:
                        self.stage = 2
                else:
                    self.p1.addPoint()
                    self.stage = 2
            else:
                if self.advantage == 1:
                    print("Player 1 wins the game!")
                    self.stage = 3 # finished
                elif self.advantage == 2:
                    self.advantage = 0
                else: # self.advantage == 0
                    self.advantage = 1
    
    def p2WinsPoint(self):
        if self.stage == 0:
            self.p2.addPoint()
        else:
            if self.stage == 1:
                if self.p2.getPoints() == 40:
                    if self.p1.getPoints() < 40:
                        print("Player 2 wins the game!")
                        self.stage = 3 # finished
                    else:
                        self.stage = 2
                else:
                    self.p2.addPoint()
                    self.stage = 2
            else:
                if self.advantage == 2:
                    print("Player 1 wins the game!")
                    self.stage = 3 # finished
                elif self.advantage == 1:
                    self.advantage = 0
                else: # self.advantage == 0
                    self.advantage = 2
                    
    def finished(self):
        return self.stage == 3
    
    def __str__(self) -> str:
        if self.stage == 0 or self.stage == 1:
            return str(self.p1) + " - " + str(self.p2)
        else:
            if self.advantage == 1:
                return "Advantage P1"
            elif self.advantage == 2:
                return "Advantage P2"
            else:
                return "Deuce"

def tennisMatch():
    """Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
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
    - Si quieres, puedes controlar errores en la entrada de datos.   
    - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos."""
    game = TennisMatch()
    while not game.finished():
        print(game)
        inp = input("P1 or P2? ")
        if inp == "P1":
            game.p1WinsPoint()
        elif inp == "P2":
            game.p2WinsPoint()
        else:
            print("Error")
            
            
if __name__ == "__main__":
    tennisMatch()