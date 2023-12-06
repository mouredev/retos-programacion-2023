/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 * 
 * Las tijeras cortan el papel, 
 * el papel envuelve la piedra, 
 * la piedra aplasta al lagarto,
 *  el lagarto envenena a Spock, 
 * Spock aplasta las tijeras,
 *  las tijeras decapitan al lagarto,
 *  el lagarto devora el papel,
 *  el papel desaprueba a Spock, 
 * Spock desintegra la piedra y, como siempre, la piedra aplasta las tijeras.
 */



function rockPaperScissorsLizardSpock(games) {
    const lista = {
        "🗿": ["🦎", "✂️"],
        "📄": ["🗿", "🖖"],
        "✂️": ["📄", "🦎"],
        "🦎": ["🖖", "📄"],
        "🖖": ["✂️", "🗿"]
    }
    let pointsP1 = 0;
    let pointsP2 = 0;
    for (const game of games) {
        const playerOne = game[0];
        const playerTwo = game[1];
        
        if (lista[playerOne].includes(playerTwo)) {
            pointsP1++;
        } else {
            pointsP2++;
        }
    }
    pointsP1 === pointsP2 ? console.log("tie") : pointsP1 > pointsP2 ? console.log("gana player 1") : console.log("gana player 2")
}

rockPaperScissorsLizardSpock([
    ["✂️", "✂️"],
    ["🦎", "🖖"],
    ["🦎", "✂️"]
])


rockPaperScissorsLizardSpock([
    ["🗿", "✂️"],
    ["✂️", "🗿"],
    ["📄", "✂️"]
])


rockPaperScissorsLizardSpock([
    ["🗿", "✂️"],
    ["🖖", "🦎"],
    ["📄", "🗿"],
  ])
