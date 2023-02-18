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

const rockPaperScissorsLizardSpock = (games) => {
  const rules = {
    "🗿": ["✂️", "🦎"],
    "📄": ["🗿", "🖖"],
    "✂️": ["📄", "🦎"],
    "🦎": ["📄", "🖖"],
    "🖖": ["🗿", "✂️"],
  };
  let playerOne = 0;
  let playerTwo = 0;

  for (const game of games) {
    const playerOneGame = game[0];
    const playerTwoGame = game[1];

    if (rules[playerOneGame].includes(playerTwoGame)) {
      playerOne++;
    } else {
      playerTwo++;
    }
  }

  return playerOne === playerTwo
    ? "Tie"
    : playerOne > playerTwo
    ? "Player 1"
    : "Player 2";
};

console.log(
  rockPaperScissorsLizardSpock([
    ["🗿", "✂️"],
    ["🖖", "🦎"],
    ["📄", "🗿"],
  ])
);
