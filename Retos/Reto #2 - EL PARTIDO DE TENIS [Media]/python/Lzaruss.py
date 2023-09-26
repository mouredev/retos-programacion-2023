"""
 Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 gane cada punto del juego.
 
 - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 - Ante la secuencia ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"], el programa mostraría lo siguiente:
   15 - Love
   30 - Love
   30 - 15
   30 - 30
   40 - 30
   Deuce
   Ventaja P1
   Ha ganado el P1
 - Si quieres, puedes controlar errores en la entrada de datos.   
 - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""

class Player:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion = 0
        self.ventaja = False

    def point(self):
        self.puntuacion += 1

    def __eq__(self, OtherPlayer: object) -> bool:
        if isinstance(OtherPlayer, Player):
            return self.puntuacion == OtherPlayer.puntuacion
        return False

    def __sub__(self, OtherPlayer:object) -> int:
        if isinstance(OtherPlayer, Player):
            if (self.puntuacion - OtherPlayer.puntuacion == 1):
                return 1
            else:
                return 0
        return -1

class Tenis:
    def __init__(self, partido:tuple):
        self.partido = partido
        self.puntuaciones = [
            'Love',
            '15',
            '30',
            '40'
        ]
        self.players = [
            Player("Alberto"),
            Player("Pablo")
        ]

    def run(self):
        for i in self.partido:
            if (i == 'P1'):
                self.players[0].point()
            else:
                self.players[1].point()
            self.printGame()
            
    def printGame(self):
        
        if (self.outGames()):
            if not (self.players[0] == self.players[1]):
                print(f'{self.puntuaciones[self.players[0].puntuacion]} - {self.puntuaciones[self.players[1].puntuacion]}')
            else:
                print("Iguales")

        elif(self.players[0] - self.players[1] == 1):
            #Comprobamos si teniamos ventaja y en ese caso ganamos
            if (self.players[0].ventaja):
                print(f"Ha ganado {self.players[0].nombre}")
                return False
            print("ventaja P1")
            self.players[0].ventaja = True 
            self.players[1].ventaja = False   
                
        elif (self.players[1] - self.players[0] == 1):
            if (self.players[1].ventaja):
                print(f"Ha ganado {self.players[1].nombre}")
                return False
            print("ventaja P2")
            self.players[1].ventaja = True
            self.players[0].ventaja = False
        else:
            if (self.players[1].puntuacion > self.players[0].puntuacion):
                print(f"Ha ganado {self.players[1].nombre}")
                return False
            elif (self.players[0].puntuacion > self.players[1].puntuacion):
                print(f"Ha ganado {self.players[0].nombre}")
                return False
            else:
                print("Deuce")
                self.ventajaFalse()

    #Metodo para ver si ya estamos en empate o ventaja
    def outGames(self) -> bool:
        if self.players[0].puntuacion >= len(self.puntuaciones) or self.players[1].puntuacion >= len(self.puntuaciones):
            return False
        else:
            return True

    def ventajaFalse(self):
        self.players[0].ventaja = False
        self.players[1].ventaja = False

if __name__ == '__main__':
    points = ("P1", "P1", "P2", "P2", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P1")
    Tenis(points).run()