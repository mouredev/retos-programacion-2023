/*
 * Crea un programa que calcule quien gana mรกs partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La funciรณn recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "๐ฟ" (piedra), "๐" (papel),
 *   "โ๏ธ" (tijera), "๐ฆ" (lagarto) o "๐" (spock).
 * - Ejemplo. Entrada: [("๐ฟ","โ๏ธ"), ("โ๏ธ","๐ฟ"), ("๐","โ๏ธ")]. Resultado: "Player 2".
 * - Debes buscar informaciรณn sobre cรณmo se juega con estas 5 posibilidades.
 */

const thisBeatsTo = {
  "๐ฟ": ["โ๏ธ", "๐ฆ"],
  "๐": ["๐ฟ", "๐"],
  "โ๏ธ": ["๐", "๐ฆ"],
  "๐ฆ": ["๐", "๐"],
  "๐": ["๐ฟ", "โ๏ธ"]
};

function play(games) {
  let balance = 0; // Perfectamente balanceado, como todas las cosas deberรญan ser

  for (let game of games) {
    if (game.length != 2) return "Deben jugar dos jugadores";
    if (!thisBeatsTo[game[0]] || !thisBeatsTo[game[1]]) return "Movimiento no vรกlido";
    if (game[0] != game[1]) thisBeatsTo[game[0]].includes(game[1]) ? balance++ : balance--;
  }

  if (balance == 0) return "Empate";
  return "Ha ganado el " + (balance > 0 ? "Jugador 1" : "Jugador 2");
}

// Ejemplo del enunciado
console.info(play([["๐ฟ", "โ๏ธ"], ["โ๏ธ", "๐ฟ"], ["๐", "โ๏ธ"]])); // 2
console.debug("----");
console.info(play([["๐ฟ", "๐"]])); // 2
console.info(play([["๐ฟ", "โ๏ธ"]])); // 1
console.info(play([["๐ฟ", "๐ฆ"]])); // 1
console.info(play([["๐ฟ", "๐"]])); // 2
console.info(play([["๐", "โ๏ธ"]])); // 2
console.info(play([["๐", "๐ฆ"]])); // 2
console.info(play([["๐", "๐"]])); // 1
console.info(play([["โ๏ธ", "๐ฆ"]])); // 1
console.info(play([["โ๏ธ", "๐"]])); // 2
console.info(play([["๐ฆ", "๐"]])); // 1
console.debug("----");
console.info(play([["๐ฟ", "๐ฟ"]])); // Empate
console.error(play([["๐ฟ"]])); // Sรณlo un jugador
console.error(play([["๐", "๐ฉ"]])); // No vรกlido