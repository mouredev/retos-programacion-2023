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

const winPlayerOne = {
  "🗿": ["✂️", "🦎"],
  "📄": ["🗿", "🖖"],
  "✂️": ["🦎", "📄"],
  "🦎": ["🖖", "📄"],
  "🖖": ["✂️", "🗿"],
};

let p1 = 0;
let p2 = 0;

function game(arr) {
  arr.map((e) => {
    if (!(e[0] === e[1])) {
      if (winPlayerOne[e[0]].includes(e[1])) {
        p1++;
      } else {
        p2++;
      }
    }
  });
  if (p1 > p2) {
    return "Player 1";
  } else if (p1 < p2) {
    return "Player 2";
  } else {
    return "Tie";
  }
}

console.log(
  game([
    ["🗿", "✂️"],
    ["✂️", "🗿"],
    ["📄", "✂️"],
  ])
);
