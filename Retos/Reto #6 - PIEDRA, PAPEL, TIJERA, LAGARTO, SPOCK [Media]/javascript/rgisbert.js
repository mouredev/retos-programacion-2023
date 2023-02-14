/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🦎" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

const objectWins = {
    "🗿": ["✂️", "🦎"],
    "📄": ["🗿", "🖖"],
    "✂️": ["📄", "🦎"],
    "🦎": ["📄", "🖖"],
    "🖖": ["🗿", "✂️"]
}

function playerWins( playerEval, oponent ) {
    return objectWins[playerEval].includes(oponent);
}

function game(plays = []) {
    const signKeys = Object.keys(objectWins);
    let player1 = 0,
        player2 = 0;

    for (const play of plays) {
        if ( play.length != 2 ) continue;
        if ( !play.every( sign => signKeys.includes(sign) ) ) continue;

        const [p1, p2] = play;

        if (playerWins(p1, p2)) player1++;
        if (playerWins(p2, p1)) player2++;
    }

    return (player1 > player2)
        ? "Player 1"
        : (player2 > player1) ? "Player 2" : "Tie"
}

console.log( game( [["🗿","✂️"], ["✂️","🗿"], ["📄","✂️"]] ) );
console.log( game( [["🗿", "📄"], ["🗿", "🖖"]] ) );
