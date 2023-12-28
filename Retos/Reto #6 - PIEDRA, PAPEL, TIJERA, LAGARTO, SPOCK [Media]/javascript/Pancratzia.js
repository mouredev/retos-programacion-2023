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
 * PROGRAMA REALIZADO POR LAURA ORTEGA - 25/08/2023
*/

const rules = {
  "✂️": ["📄", "🦎"], //Tijera corta al papel y decapita al lagarto
  "📄": ["🗿", "🖖"], //Papel tapa piedra y desautoriza a Spock
  "🗿": ["🦎", "✂️"], //Piedra aplasta a lagarto y a tijera
  "🦎": ["🖖", "📄"], //Lagarto come papel y envenena a Spock
  "🖖": ["✂️", "🗿"], //Spock vaporiza a la piedra y rompe tijera
}


const rpsls = game => {
    let player1 = 0, player2 = 0;

    game.forEach(round => {
        const [p1, p2] = round;

        switch (true) {
            case rules[p1].includes(p2):
                player1++;
                break;
            case rules[p2].includes(p1):
                player2++;
                break;
            default:
                break;
        }
    });

    return player1 > player2 ? "Player 1" : (player2 > player1) ? "Player 2" : "Tie";
}

console.log(rpsls([['🗿','✂️'], ['✂️','🗿'], ['📄','✂️']])) // Player 2
console.log(rpsls([["✂️", "✂️"], ["🦎", "🖖"], ["🦎", "✂️"]])) // Tie
console.log(rpsls([["🗿", "🗿"], ["🗿", "🗿"], ["🗿", "🗿"], ["🗿", "🗿"]])) // Tie
console.log(rpsls([["🦎", "🗿"], ["📄", "🦎"], ["🖖", "✂️"], ["🗿", "🖖"], ["✂️", "🦎"]])) // Player 2
console.log(rpsls([["📄", "🖖"], ["🦎", "🗿"], ["🖖", "🦎"], ["✂️", "📄"], ["🖖", "📄"], ["🗿", "✂️"], ["🦎", "🖖"]])) // Player 1
