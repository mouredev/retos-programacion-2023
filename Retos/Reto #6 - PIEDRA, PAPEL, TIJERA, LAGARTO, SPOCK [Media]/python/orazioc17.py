from typing import List


class Juego:

    jugador_1 = 0
    jugador_2 = 0

    PIEDRA = 'piedra'
    PAPEL = 'papel'
    TIJERA = 'tijera'
    LAGARTO = 'lagarto'
    SPOCK = 'spock'

    manos = [PIEDRA, TIJERA, PAPEL, LAGARTO, SPOCK]

    gana_contra = {
        PIEDRA: [LAGARTO, TIJERA],
        PAPEL: [PIEDRA, SPOCK],
        TIJERA: [PAPEL, LAGARTO],
        LAGARTO: [SPOCK, PAPEL],
        SPOCK: [TIJERA, PIEDRA]
    }

    def comprobar_errores(self, jugadas: List[tuple]):
        if len(jugadas) == 0:
            return True, 'Lista vacia'
        for jugada in jugadas:
            if type(jugada) is not tuple:
                return True, 'Algun dato de la lista no es una tupla'
            if jugada[0].lower() not in self.manos or jugada[1].lower() not in self.manos:
                return True, 'Error en la entrada de movimientos'
        
        return False, ''

    def gameloop(self, jugadas: List[tuple]):
        for jugada in jugadas:
            if jugada[0].lower() == jugada[1].lower():
                continue
            else:
                if jugada[1].lower() in self.gana_contra[jugada[0].lower()]:
                    self.jugador_1 += 1
                else:
                    self.jugador_2 += 1

    def resultado(self):
        if self.jugador_1 == self.jugador_2:
            print('Tie')
        elif self.jugador_1 > self.jugador_2:
            print('Player 1')
        else:
            print('Player 2')
            
    def jugar(self, jugadas: List[tuple]):

        hay_error, mensaje = self.comprobar_errores(jugadas)
        if hay_error:
            print(mensaje)
        else:
            self.gameloop(jugadas)
        
        self.resultado()

        self.jugador_1 = 0
        self.jugador_2 = 0


def run():
    juego = Juego()
    juego.jugar((('spock', 'lagarto'), ('tijera', 'piedra'), ('papel', 'spock'), ('TIJERA', 'PIEDRA')))  # Player 2
    juego.jugar((('papel', 'Spock'), ('tijera', 'lagarto'), ('piedra', 'papel'), ('spock', 'tijera'), ('lagarto', 'spock')))  # Player 1
    juego.jugar((('piedra', 'piedra'), ('tijera', 'papel'), ('papel', 'tijera')))  # Tie


if __name__ == '__main__':
    run()
