lista <- list('P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1')
puntuaciones <- list("love", '15', '30', '40')
jugador_1 = 0
jugador_2 = 0

for (i in lista) {

    if (i == 'P1') {
        jugador_1 <- jugador_1 + 1
    }

    if (i == 'P2') {
        jugador_2 <- jugador_2  + 1
    }
   
    if (jugador_1 == 3 & jugador_2 == 3) {
        print('Deuce')
    } else {

        diff <- jugador_1 - jugador_2

        if (diff == 0) {
            print('Deuce')
        } else if (diff == 1) {
            print('Ventaja P1')
        } else if (diff == -1) {
            print('Ventaja P2')
        } else if (diff >= 2) {
            print('Ha ganado P1')
        } else {
            print('Ha ganado P2')
        }
    }

}