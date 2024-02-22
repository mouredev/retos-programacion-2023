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

const stonePaperScissorsLizardSpock = (arg) => {
    
    let = player1 = 0, player2 = 0;

    for (const element of arg) {
        if (element.player1 === "🗿") {
            if (element.player2 === "✂️" || element.player2 === "🦎") player1++;
        }
        if (element.player1 === "📄") {
            if (element.player2 === "🗿" || element.player2 === "🖖") player1++;
        }
        if (element.player1 === "✂️" ) {
            if (element.player2 === "📄" || element.player2 === "🦎") player1++;
        }
        if (element.player1 === "🦎" ) {
            if (element.player2 === "📄" || element.player2 === "🖖") player1++;
        }
        if (element.player1 === "🖖") {
            if (element.player2 === "🗿" || element.player2 === "✂️") player1++;
        }
        
        if (element.player2 === "🗿") {
            if (element.player1 === "✂️" || element.player1 === "🦎") player2++;
        }
        if (element.player2 === "📄") {
            if (element.player1 === "🗿" || element.player1 === "🖖") player2++;
        }
        if (element.player2 === "✂️" ) {
            if (element.player1 === "📄" || element.player1 === "🦎") player2++;
        }
        if (element.player2 === "🦎" ) {
            if (element.player1 === "📄" || element.player1 === "🖖") player2++;
        }
        if (element.player2 === "🖖") {
            if (element.player1 === "🗿" || element.player1 === "✂️") player2++;
        }
    } 
     return player1 === player2 ? "Tie" : player1 > player2 ? "Player 1" :"Player 2"

}

const firstGame = [{player1:"🗿", player2:"✂️"}, {player1:"✂️", player2:"🗿"}, {player1:"📄", player2:"✂️"}]

const secondGame = [{player1:"🦎",  player2:"🖖"}, {player1:"✂️", player2:"🦎"}, {player1:"✂️", player2:"✂️"},
{player1:"🗿",  player2:"🖖"}, {player1:"✂️", player2:"✂️"}, {player1:"📄", player2:"📄"}]

const thirdGame = [{player1:"🗿",  player2:"✂️"}, {player1:"✂️", player2:"🗿"}, {player1:"📄", player2:"✂️"},
{player1:"🗿",  player2:"🦎"}, {player1:"✂️", player2:"🦎"}, {player1:"📄", player2:"✂️"}]

console.log(stonePaperScissorsLizardSpock(firstGame))
console.log(stonePaperScissorsLizardSpock(secondGame))
console.log(stonePaperScissorsLizardSpock(thirdGame))