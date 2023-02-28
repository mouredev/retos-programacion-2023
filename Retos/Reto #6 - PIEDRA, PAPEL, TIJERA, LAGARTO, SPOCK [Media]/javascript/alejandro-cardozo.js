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

/**
 *  Retrieves the winner of a Rock-Paper-Scissors-Lizard-Spock match
 *  @param {Array} arr 2D_Array where each subarray represents a game of the match
 *  @returns {string} String with the winning player or tie if both won the same number of games
 */
function RockPaperScissorsLizardSpock(arr) {
  const rules = {
    '🗿': ['✂️', '🦎'],
    '📄': ['🗿', '🖖'],
    '✂️': ['📄', '🦎'],
    '🦎': ['📄', '🖖'],
    '🖖': ['🗿', '✂️'],
  };
  const results = arr.reduce(
    (acc, el) => {
      if (el[0] === el[1]) return acc;
      return rules[el[0]].includes(el[1])
        ? [acc[0] + 1, acc[1]]
        : [acc[0], acc[1] + 1];
    },
    [0, 0]
  );
  return results[0] > results[1]
    ? 'Player 1'
    : results[0] < results[1]
    ? 'Player 2'
    : 'Tie';
}


// Test
// console.log(
//   RockPaperScissorsLizardSpock([
//     ['🗿', '✂️'],
//     ['🗿', '🖖'],
//     ['📄', '✂️'],
//     ['🗿', '✂️'],
//     ['📄', '🦎'],
//   ])
// );
