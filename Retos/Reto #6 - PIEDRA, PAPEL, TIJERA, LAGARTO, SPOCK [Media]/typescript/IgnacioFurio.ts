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
const results: [any, any][] = [["🗿","✂️"], ["✂️","🗿"], ["📄","🖖"]];

const sheldonGame = (arr: any) => {
    const rounds: any[] = arr;
    const winConditions: any = {
        "🗿": ["✂️", "🦎"],
        "📄": ["🖖", "🗿"],
        "✂️": ["📄", "🦎"],
        "🦎": ["📄", "🖖"],
        "🖖": ["✂️", "🗿"]
    };
    
    let player1: number = 0;
    let player2: number = 0;

    let winner: string = "";

    for (let i = 0; i < rounds.length; i++) {
        for (let j = 0; j < rounds[i].length; j++) {
            if (j % 2 === 0) { /*comparamos si el player1 gana la ronda*/
                for (let k = 0; k < winConditions[rounds[i][j]].length; k++) {                    
                    if (rounds[i][j + 1] === winConditions[rounds[i][j]][k]) player1 ++;
                };
                
            } else if (j % 2 !== 0) { /*comparamos si el player2 gana la ronda*/
                for (let k = 0; k < winConditions[rounds[i][j]].length; k++) {                    
                    if (rounds[i][j + -1] === winConditions[rounds[i][j]][k]) player2 ++;
                };                
            };
            //declaramos el ganador al mejor de 3 rondas
            if (player1 === 2 ) {
                winner = "Player 1";
                break;
            } else if (player2 === 2 ) {
                winner = "Player 2";
                break;
            };
        };
        //declaramos empate si ningún jugador consigue ganar dos rondas
        if (player1 === 1 && player2 === 1) {
            winner = "Empate";            
        }
    };

    return winner;
};

sheldonGame(results);