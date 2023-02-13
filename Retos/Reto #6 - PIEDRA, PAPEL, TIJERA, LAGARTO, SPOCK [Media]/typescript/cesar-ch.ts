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

const winPlayer1: { [key: string]: Array<string> } = {
  "🗿": ["✂️", "🦎"],
  "📄": ["🗿", "🖖"],
  "✂️": ["🦎", "📄"],
  "🦎": ["🖖", "📄"],
  "🖖": ["✂️", "🗿"],
};

let player1 = 0;
let player2 = 0;

function playGame(arr: Array<Array<string>>): string {
  arr.forEach((e) => {
    if (!(e[0] === e[1])) {
      if (winPlayer1[e[0]] && winPlayer1[e[0]].includes(e[1])) {
        player1++;
      } else {
        player2++;
      }
    }
  });
  if (player1 > player2) {
    return "Player 1";
  } else if (player1 < player2) {
    return "Player 2";
  } else {
    return "Tie";
  }
}

console.log(
  playGame([
    ["🗿", "✂️"],
    ["✂️", "🗿"],
    ["📄", "✂️"],
  ])
);
