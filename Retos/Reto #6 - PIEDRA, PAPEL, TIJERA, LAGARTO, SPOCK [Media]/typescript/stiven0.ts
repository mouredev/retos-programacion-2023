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

type gameOptions  = '🗿' | '📄' | '✂️' | '🦎' | '🖖';
type gameResult = 'Player 1' | 'Player 2' | 'Tie';

const winning_moves = {
    '🗿' : ['✂️', '🦎'],
    '📄' : ['🗿', '🖖'],
    '✂️' : ['📄', '🦎'],
    '🦎' : ['🖖', '📄'],
    '🖖' : ['✂️', '🗿']
}

const startGame = ( game: gameOptions[][] ): gameResult => {

    const marker = {
        player1: 0,
        player2: 0
    }    
    
    for ( const match of game ) {

        if ( winning_moves[ match[0] ].includes( match[1] ) ) {
            marker[ 'player1' ] += 1;
        } else if ( winning_moves[ match[1] ].includes( match[0] ) ) {
            marker[ 'player2' ] += 1;
        }

    }

    const { player1, player2 } = marker;
    return player1 > player2 ? 'Player 1' : player2 > player1 ? 'Player 2' : 'Tie';

}

console.log( startGame( [ ['🗿', '✂️'], ['🦎', '📄'], ['✂️', '🦎'] ] ) );