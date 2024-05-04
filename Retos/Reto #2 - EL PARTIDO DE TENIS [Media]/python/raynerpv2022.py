
# Reto #2: EL PARTIDO DE TENIS
# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   



# input
game_1 = [1,1,1,2,2,2,1,2,1,2,1,2,1,2,2,2] 

def tennis_game(score):
    print(" ********* Tennis GAme *************")
    p1 = 0
    p2 = 0
    for  i in score:

        match i:
            case 1: 
                match p1:
                    case 0 | 15:
                        p1+=15
                    case n if n >=30:
                        p1+=10
            case 2:
                match p2:
                    case 0 | 15:
                        p2+=15
                    case n if n >= 30:
                        p2+=10

        print(i)
        
        if (p1 > 50) and (p2+20 <= p1):
            print("Gana  P1")
            break
        if (p2 > 50) and (p1+20 <= p2):
            print("Gana  P2")
            break
        
        if p1 == p2 and p1 >=40:
            print("deuce")
            continue
        if (p1 > 40) and (p2+10 <= p1):
            print("Ventaja de P1")
            continue

        if (p2 > 40) and (p1+10 <= p2):
            print("Ventaja de P2")
            continue

        print(p1, p2)

tennis_game(game_1)
a = 51
print("hello" if a == 5 else "hola")
             
#  other example with class

class TennisGame():
    def __init__(self) -> None:
        self.p1 = 0
        self.p2 = 0
        self.final = 0
        self.score = {0:"LOVE",1:15,2:30,3:40,4:"DEUCE", 5: "GANA P1",6:"VENTAJA P1",7:"GANA P2", 8:"VENTAJA P2"}
    
    def point_p1(self):
        self.p1 +=1

    def point_p2(self):
        self.p2 +=1
    
    def score_board(self,score):
        return self.score.get(score)
    
    def game(self,score):
         print("***************** GAME Tennis ***************")
         for i in score:
            if i == 1:
                   self.point_p1()
            if i == 2:
                    self.point_p2()

            #  if are equal and have more than 30 point
            if self.p1 > 2 and self.p1 == self.p2:
                    self.final = 4 
                    print(self.score_board(self.final))
                    continue
            
            #  if p1 greater than 30
            if self.p1 > 3 :
                # and more than 2 point of diference, win
                if self.p2 +2 <= self.p1:
                    self.final = 5
                    print(self.score_board(self.final))
                    break
                # and monly one point of diference, ventaja
                if self.p2 +1 <= self.p1:
                    self.final = 6 
                    print(self.score_board(self.final))
                    continue
            if self.p2 > 3 :
                if self.p1 +2 <= self.p2:
                    self.final = 7 
                    print(self.score_board(self.final))
                    break
                if self.p1 +1 <= self.p2:
                     self.final = 8
                     print(self.score_board(self.final))
                     continue

            #  between 0 and 30 
            print(self.score_board(self.p1), self.score_board(self.p2))
    
    
        
                


juego = TennisGame()
juego.game([1,1,1,2,2,2,1,2,1,2,1,2,1,2,2,2])


juego2 = TennisGame()
juego2.game([1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1])


