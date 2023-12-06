/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

/**
 * Tipado de las opciones de juego
 */
type Options = "🗿" | "📄" | "✂️" | "🦎" | "🖖"


/**
 * Enumerado que representa un resultado de una jugada.
 */
enum Result  {
    Tie = 0,
    Player1 = 1,
    Player2= 2
}

/**
 * Clase que representa una jugada
 */
class Game{
    listOfGames : [Options, Options][]
    namePlayer1 : string
    namePlayer2 : string
    constructor(list : [Options, Options][], namePlayer1 : string, namePlayer2 : string){
        this.listOfGames = list
        this.namePlayer1 = namePlayer1
        this.namePlayer2 = namePlayer2
    }


}
/**
 * Funcion que busca el ganador si lo hay de una lista de jugadas
 * @param listOfGame Listado de jugadas
 * @return Resultado de la jugada
 * @see Result
 */
function foundWinner(listOfGame:Result[]) : Result {

    const player1 = listOfGame.filter((game) => game === Result.Player1).length
    const player2 = listOfGame.filter((game) => game === Result.Player2).length


    if (player1 > player2) {
        return Result.Player1
    }else if (player2 > player1) {
        return Result.Player2
    } else {
        return Result.Tie
    }

}
/**
 * Funcion que evalua una partida de piedra, papel, tijera
 * @param game objeto que representa un juego con los jugadores y las jugadas de cada uno
 * @return String con el nombre del jugador o empate en el que no hay ningun ganador
 */
function evaluateGame(game : Game) : string {

    const array = game.listOfGames.map((it) =>{
        switch (JSON.stringify(it)) {

            case JSON.stringify(["🗿", "✂️"]): return Result.Player1
            case JSON.stringify(["✂️", "🗿"]): return Result.Player2

            case JSON.stringify(["📄", "✂️"]): return Result.Player2
            case JSON.stringify(["✂️", "📄"]): return Result.Player1

            case JSON.stringify(["🗿", "📄"]): return Result.Player2
            case JSON.stringify(["📄", "🗿"]): return Result.Player1

            case JSON.stringify(["🦎", "🗿"]): return Result.Player2
            case JSON.stringify(["🗿", "🦎"]): return Result.Player1

            case JSON.stringify(["🦎", "📄"]): return Result.Player1
            case JSON.stringify(["📄", "🦎"]): return Result.Player2

            case JSON.stringify(["🖖", "📄"]): return Result.Player2
            case JSON.stringify(["📄", "🖖"]): return Result.Player1

            case JSON.stringify(["🖖", "🗿"]): return Result.Player1
            case JSON.stringify(["🗿", "🖖"]): return Result.Player2

            case JSON.stringify(["🖖", "✂️"]): return Result.Player1
            case JSON.stringify(["✂️", "🖖"]): return Result.Player2

            case JSON.stringify(["🖖", "🦎"]): return Result.Player2
            case JSON.stringify(["🦎", "🖖"]): return Result.Player1

            case JSON.stringify(["🦎", "✂️"]): return Result.Player2
            case JSON.stringify(["✂️", "🦎"]): return Result.Player1


            default: return Result.Tie

        }
    })

       switch (foundWinner(array)) {
           case Result.Player1:
               return `Gana el jugador ${game.namePlayer1}`
           case Result.Player2:
               return `Gana el jugador ${game.namePlayer2}`
           case Result.Tie: return `empate`

       }



}

/**
 * Casos de prueba
 */

const game = new Game(
    [
        ["🗿", "✂️"],
        ["✂️", "🗿"],
        ["🦎", "✂️"],
        ["🗿", "📄"],
        ["📄", "🗿"],
        ["🗿", "🗿"],
        ["🖖", "🦎"],
        ["🖖", "✂️"],



    ], "Player 1", "Player 2")


console.log(`el resultado es: ${evaluateGame(game)}`)

const game2 = new Game(
    [
        ["🗿", "✂️"],
        ["🦎", "✂️"],
        ["🖖", "🗿"],
        ["🖖", "🖖"],

    ], "Player 1", "Player 2")


console.log(`el resultado es: ${evaluateGame(game2)}`)

const game3 = new Game(
    [
        ["🖖", "🦎"],
        ["🦎", "🖖"],
        ["🖖", "🖖"],

    ], "Player 1", "Player 2")


console.log(`el resultado es: ${evaluateGame(game3)}`)