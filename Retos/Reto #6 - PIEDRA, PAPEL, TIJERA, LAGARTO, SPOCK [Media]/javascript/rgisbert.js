/*
 * Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
 *   "βοΈ" (tijera), "π¦" (lagarto) o "π¦" (spock).
 * - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
 * - Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.
 */

const objectWins = {
    "πΏ": ["βοΈ", "π¦"],
    "π": ["πΏ", "π"],
    "βοΈ": ["π", "π¦"],
    "π¦": ["π", "π"],
    "π": ["πΏ", "βοΈ"]
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

console.log( game( [["πΏ","βοΈ"], ["βοΈ","πΏ"], ["π","βοΈ"]] ) );
console.log( game( [["πΏ", "π"], ["πΏ", "π"]] ) );
