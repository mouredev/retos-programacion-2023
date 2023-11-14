/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [["🗿","✂️"], ["✂️","🗿"], ["📄","✂️"]]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

const retoSeis = games => {
  const rules = {
    "✂️": ["📄", "🦎"],
    "📄": ["🗿", "🖖"],
    "🗿": ["🦎", "✂️"],
    "🦎": ["🖖", "📄"],
    "🖖": ["✂️", "🗿"],
  };

  let player1 = 0, player2 = 0;

  for (const game of games) {
    let player1_game = game[0];
    let player2_game = game[1];

    if (player1_game === player2_game) continue;

    if(rules[player1_game].includes(player2_game)){
      player1++;
    } else if (rules[player2_game].includes(player1_game)){
      player2++;
    }
  }

  return (player1 === player2)? 'Tie': (player1 > player2)? 'Player 1': 'Player 2';
};

console.log(retoSeis([["🗿", "✂️"]]));
console.log(retoSeis([["🗿", "🗿"]]));
console.log(retoSeis([["✂️", "🗿"]]));
console.log(retoSeis([["🗿","✂️"], ["✂️","🗿"], ["📄","✂️"]]));
console.log(retoSeis([["🗿", "🗿"], ["🗿", "🗿"], ["🗿", "🗿"], ["🗿", "🗿"]]));
console.log(retoSeis([["🖖", "🗿"], ["✂️", "📄"], ["🗿", "🗿"], ["🦎", "🖖"]]));