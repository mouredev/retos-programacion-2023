// Crea un programa que calcule quien gana más partidas al piedra,
// papel, tijera, lagarto, spock.
// - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
// - La función recibe un listado que contiene pares, representando cada jugada.
// - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
//   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
// - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
// - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

const winsAgainst = {
    '🗿': ['✂️', '🦎'],
    '📄': ['🗿', '🖖'],
    '✂️': ['📄', '🦎'],
    '🦎': ['📄', '🖖'],
    '🖖': ['✂️', '🗿'],
};

function playGame(gameArray) {
    let player1Score = 0;
    let player2Score = 0;
    for (let i = 0; i < gameArray.length; i++) {
        const player1Emoji = gameArray[i][0];
        const player2Emoji = gameArray[i][1];
        console.log(`Game ${i + 1}:`);
        console.log(`Player1: ${player1Emoji} | Player2: ${player2Emoji}`);
        if (winsAgainst[player1Emoji].includes(player2Emoji)) {
            console.log('Point for player 1');
            player1Score++;
        } else {
            console.log('Point for player 2');
            player2Score++;
        }
        console.log('---------------------------');
    }
    console.log('===========================');
    if (player1Score > player2Score) {
        console.log('🏆 Player 1 wins the game!');
    } else if (player2Score > player1Score) {
        console.log('🏆 Player 2 wins the game!');
    } else {
        console.log("It's a tie!");
    }
}

const gameInput = [
    ['🗿', '✂️'],
    ['✂️', '🗿'],
    ['📄', '✂️'],
];

playGame(gameInput);
