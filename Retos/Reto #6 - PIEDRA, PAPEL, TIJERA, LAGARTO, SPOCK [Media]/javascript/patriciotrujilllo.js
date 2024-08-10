
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


function jankenpo(play) {

    listaResultados = {
        "🗿": { "🗿": "Tie", "✂️": "Player1", "📄": "Player2", "🦎": "Player1", "🖖": "Player2" },
        "📄": { "🗿": "Player1", "✂️": "Player2", "📄": "Tie", "🦎": "Player2", "🖖": "Player1" },
        "✂️": { "🗿": "Player2", "✂️": "Tie", "📄": "Player1", "🦎": "Player1", "🖖": "Player2" },
        "🦎": { "🗿": "Player2", "✂️": "Player2", "📄": "Player1", "🦎": "Tie", "🖖": "Player1" },
        "🖖": { "🗿": "Player1", "✂️": "Player1", "📄": "Player2", "🦎": "Player2", "🖖": "Tie" }
    }

    let player1 = 0, player2 = 0, tie = 0

    play.forEach(element => {
        for (let clave in listaResultados) {

            if (clave === element[0]) {

                let ganador = listaResultados[clave][element[1]]
                if (ganador === 'Player1') player1 += 1
                if (ganador === 'Player2') player2 += 1
                else tie += 1
            }
        }
    })

    if (player1 > player2) return 'El ganador es el Player 1'
    else if (player1 < player2) return 'El ganador es el Player 2'
    else return 'Es empate'
}

console.log(jankenpo([["🗿", "✂️"], ["✂️", "🗿"], ["📄", "✂️"]]))
console.log(jankenpo([["🗿", "✂️"], ["✂️", "🗿"], ["✂️", "✂️"]]))
console.log(jankenpo([["🗿", "✂️"], ["✂️", "🗿"], ["🦎", "📄"]]))