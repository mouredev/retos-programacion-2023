// Reto 6 joaquinpolom

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
/* Resultados
  '🗿': ['✂️', '🦎'],
  '📃': ['🗿', '🖖🏻'],
  '✂️': ['📃', '🦎'],
  '🦎': ['📃', '🖖🏻'],
  '🖖🏻': ['✂️', '🗿'],
 */

// Table with the rules of the game
let results = {
  '🗿': ['✂️', '🦎'],
  '📃': ['🗿', '🖖'],
  '✂️': ['📃', '🦎'],
  '🦎': ['📃', '🖖'],
  '🖖': ['✂️', '🗿'],
};

// Initialising points of the game
let gameResult = [
  Player1 = 0,
  Player2 = 0,
  Tie = 0,
  ];
  
// Entry
let game1 = [['🗿','✂️'], ['✂️','🗿'], ['📃','✂️']]; // "Player2"
let game2 = [['✂️','🗿'], ['📃','🖖'], ['🦎','🖖'], ['🖖','✂️']]; // "Player1"

function pptle(game) {
  // Reset the results
  gameResult.Player1 = 0;
  gameResult.Player2 = 0;
  gameResult.Tie = 0;
  // Check every result
  for (const a of game) {
    // Guest player1
    let gp1 = a[0];
    // Guest player2
    let gp2 = a[1];
    // if it is the same result then tie
    if (gp1 === gp2) {
      // Tie
      gameResult.Tie += 1;
    } else {
      // Who win that game
      // Check table results. Result1 will have the options that loose against player1
      var result1 = results[gp1];
      // if guest player2 is in result1 Player1 win if not Player2 wins
      if ((gp2 === result1[0]) || (gp2 === result1[1])) {
        // wins player1
        gameResult.Player1 += 1;
      } else {
        // wins player2
        gameResult.Player2 += 1;
      }
    }
  }
  // Check the final result
  if ((gameResult.Tie > gameResult.Player1) || (gameResult.Tie > gameResult.Player2) || (gameResult.Player1 === gameResult.Player2)) {
    //Tie
    return "Tie";
  } else if (gameResult.Player1 > gameResult.Player2) {
    // Win Player1
    return "Player1";
  } else {
    // Win Player2
    return "Player2";
  }
}

console.log(game1);
console.log(pptle(game1));
console.log(game2);
console.log(pptle(game2));
