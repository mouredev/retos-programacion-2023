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

const thisBeatsTo = {
  "🗿": ["✂️", "🦎"],
  "📄": ["🗿", "🖖"],
  "✂️": ["📄", "🦎"],
  "🦎": ["📄", "🖖"],
  "🖖": ["🗿", "✂️"]
};

function play(games) {
  let balance = 0; // Perfectamente balanceado, como todas las cosas deberían ser

  for (let game of games) {
    if (game.length != 2) return "Deben jugar dos jugadores";
    if (!thisBeatsTo[game[0]] || !thisBeatsTo[game[1]]) return "Movimiento no válido";
    if (game[0] != game[1]) thisBeatsTo[game[0]].includes(game[1]) ? balance++ : balance--;
  }

  if (balance == 0) return "Empate";
  return "Ha ganado el " + (balance > 0 ? "Jugador 1" : "Jugador 2");
}

// Ejemplo del enunciado
console.info(play([["🗿", "✂️"], ["✂️", "🗿"], ["📄", "✂️"]])); // 2
console.debug("----");
console.info(play([["🗿", "📄"]])); // 2
console.info(play([["🗿", "✂️"]])); // 1
console.info(play([["🗿", "🦎"]])); // 1
console.info(play([["🗿", "🖖"]])); // 2
console.info(play([["📄", "✂️"]])); // 2
console.info(play([["📄", "🦎"]])); // 2
console.info(play([["📄", "🖖"]])); // 1
console.info(play([["✂️", "🦎"]])); // 1
console.info(play([["✂️", "🖖"]])); // 2
console.info(play([["🦎", "🖖"]])); // 1
console.debug("----");
console.info(play([["🗿", "🗿"]])); // Empate
console.error(play([["🗿"]])); // Sólo un jugador
console.error(play([["💀", "💩"]])); // No válido