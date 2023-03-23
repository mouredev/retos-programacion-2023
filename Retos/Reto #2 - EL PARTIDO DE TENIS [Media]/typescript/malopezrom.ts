/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 */

/**
 * Enumerado de los jugadores
 * @type {{P1: string; P2: string}}
 */
enum Players {
    P1 = "P1",
    P2 = "P2"
}

/**
 * Enum Score
 * Representa el score de un jugador
 */
enum Score {
    Love,
    Fifteen,
    Thirty ,
    Forty,
    Deuce ,
    Advantage,
    Winner

}

/**
 * Clase Player.
 * Representa un jugador con su nombre y su puntacion
 */
class Player {
    name:Players;
    score:Score;
    constructor(name:Players, score:Score){
        this.name = name;
        this.score = score;
    }
}

/**
 * Funcion principal del juego de tenis
 * Recibe un array de jugadores que han ganado cada punto*
 * @param gamesSequence Array de {Players} que han ganado cada punto
 */
function matchPoint(gamesSequence:Array<Players>){

    let player1 = new Player(Players.P1, Score.Love);
    let player2 = new Player(Players.P2, Score.Love);


    gamesSequence.every((game) => {

        if(game === Players.P1)
            point(player1,player2)
        else point(player2,player1)


        if(hasWinner(player1,player2))
            return false
        else
            console.log(printScore(player1) + " - " + printScore(player2))
        return true



    })

    if(!hasWinner(player1,player2))
        console.log("No hay ganador")
    else
        console.log("Ganador " +  (player1.score===Score.Winner ? player1.name:player2.name))




}

/**
 * Lógica de puntuaación del juego.
 * Suma un punto al jugador que ha ganado el punto.
 * Si ambos jugadores tienen 40 puntos, se produce un empate (Deuce).
 * Si un jugador tiene ventaja, gana el juego.(Winner)
 * @param playerWin Player que ha ganado el punto
 * @param playerLose Player que ha perdido el punto
 */

function point(playerWin:Player,playerLose:Player){


    switch (playerWin.score) {
        case Score.Love:
            playerWin.score++
            break;
        case Score.Fifteen:
            playerWin.score++
            break;
        case Score.Thirty:
            playerWin.score++
            break;
        case Score.Forty:
            if(playerLose.score === Score.Forty){
                playerWin.score = Score.Advantage;
            }
            else if(playerLose.score === Score.Advantage){
                playerLose.score = Score.Forty;
            }else{
                playerWin.score = Score.Winner;
            }
            break;
        case Score.Deuce:
            playerWin.score = Score.Advantage;
            break;
        case Score.Advantage:
            playerWin.score = Score.Winner;
            break;
    }
}

/**
 * Imprime el score del jugador
 * @param p1 Player a imprimir
 */
function printScore(p1:Player){
    switch (p1.score) {
        case Score.Love:
            return "Love"
        case Score.Fifteen:
            return "15"
        case Score.Thirty:
            return "30"
        case Score.Forty:
            return "40"
        case Score.Deuce:
            return "Deuce"
        case Score.Advantage:
            return "Adv"

    }

}

/**
 * Comprueba si alguno de los jugadores ha ganado
 * @param p1 Player 1
 * @param p2 Player 2
 * @returns {boolean} true si alguno de los jugadores ha ganado
 */
function hasWinner(p1:Player,p2:Player):boolean{
    return p1.score === Score.Winner || p2.score === Score.Winner

}

// Test cases
matchPoint([Players.P1,Players.P1,Players.P1,Players.P1,Players.P2])
matchPoint([Players.P1,Players.P1,Players.P1,Players.P2,Players.P2,Players.P2,Players.P2,Players.P1,Players.P1,Players.P2,Players.P2,Players.P2])
matchPoint([Players.P1,Players.P1,Players.P1])