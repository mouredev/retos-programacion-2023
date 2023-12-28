#
# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# gane cada punto del juego.
#
# - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#   15 - Love
#   30 - Love
#   30 - 15
#   30 - 30
#   40 - 30
#   Deuce
#   Ventaja P1
#   Ha ganado el P1
# - Si quieres, puedes controlar errores en la entrada de datos.
# - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
#

class Partido_tenis:
    def __init__(self):
        self.puntaje = ["Love", "15", "30", "40"]
        self.estado = ""
        self.ganador = False

    def calcula_puntaje(self, p1, p2):
        if p1 > 3 or p2 > 3:
            if p1 == p2:
                self.estado = "Deuce"
            elif p1 - p2 == 2:
                self.estado = "Ha ganado el P1"
                self.ganador = True
            elif p2 - p1 == 2:
                self.estado = "Ha ganado el P2"
                self.ganador = True
            elif p1 > p2:
                self.estado = "Ventaja P1"
            elif p2 > p1:
                self.estado = "Ventaja P2"
            elif p1 == 3 and p2 == 3:
                self.estado = "Deuce"
        elif p1 == 3 and p2 == 3:
            self.estado = "Deuce"
        else:
            self.estado = f"{self.puntaje[p1]} - {self.puntaje[p2]}"

        return self.estado, self.ganador

    def partido(self, secuencia):
        p1 = 0
        p2 = 0
        ganador = False
        puntaje = ""
        # Recorremos la secuencia para encontrar al ganador
        for turno in secuencia:
            if turno == "P1":
                p1 += 1
            else:
                p2 += 1

            puntaje, ganador = self.calcula_puntaje(p1, p2) 
           
            print(puntaje)
            if ganador:
                quit()

        if ganador == False:
            print("Datos incompletos")

if __name__ == "__main__":

    secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
    tenis = Partido_tenis()
    tenis.partido(secuencia)