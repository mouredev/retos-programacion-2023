/**
 * Crea un programa que calcule quien gana más
 * partidas al piedra, papel, tijera, lagarto,
 * spock.
 * - El resultado puede ser: "Player 1",
 * "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene
 * pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿"
 * (piedra), "📄" (papel),
 * "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo.
 * Entrada: [
 * ("🗿","✂️"),
 * ("✂️","🗿"),
 * ("📄","✂️")
 * ].
 * Resultado: "Player 2".
 * - Debes buscar información sobre cómo se
 * juega con estas 5 posibilidades.
 * 
 * 
 * www.retosdeprogramacion.com
 */

const play = [
  ["🗿", "📄"],
  ["✂️", "📄"],
  ["✂️", "📄"],
];
const rules = {
  "🗿": ["🦎", "✂️"],
  "✂️": ["📄", "🦎"],
  "📄": ["🗿", "🖖"],
  "🦎": ["🖖", "📄"],
  "🖖": ["✂️", "🗿"],
};

const getWinner = (arr) => {
  let player1 = 0;
  let player2 = 0;
  arr.forEach(play => {
    if (rules[play[0]].includes(play[1])) {
      player1 += 1;
    } else if (rules[play[1]].includes(play[0])) {
      player2 += 1;
    }
  });
  if (player1 > player2) {
    return 'Player 1';
  } else if (player2 > player1) {
    return 'Player 2';
  } else {
    return 'Tie';
  }
}

console.log(getWinner(play));
