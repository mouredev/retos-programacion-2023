/* Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades. 
- Las tijeras cortan el papel
- El papel cubre la piedra
- La piedra aplasta al lagarto
- El lagarto envenena a Spock
- Spock rompe las tijeras
- Las tijeras decapitan al lagarto
- El lagarto come el papel
- El papel desacredita a Spock
- Spock vaporiza la piedra
- La piedra aplasta las tijeras*/

let playerOne: number = 0;
let playerTwo: number = 0;

const plays = [
  [
    ['🗿', '✂️'],
    ['✂️', '🗿'],
    ['📄', '✂️'],
  ],
  [
    ['🗿', '✂️'],
    ['🗿', '🗿'],
    ['🖖', '✂️'],
  ],
  [
    ['🗿', '✂️'],
    ['✂️', '🗿'],
    ['📄', '✂️'],
    ['🗿', '✂️'],
  ],
];

const points = (playOne: string, playTwo: string): void => {
  if (playOne === playTwo) {
    // tie
    playerOne++;
    playerTwo++;
  } else if (
    //  player one wins!
    (playOne === '🖖' && playTwo === '✂️') ||
    (playOne === '✂️' && playTwo === '📄') ||
    (playOne === '📄' && playTwo === '🗿') ||
    (playOne === '🗿' && playTwo === '🦎') ||
    (playOne === '🦎' && playTwo === '🖖') ||
    (playOne === '📄' && playTwo === '🖖') ||
    (playOne === '🖖' && playTwo === '🗿') ||
    (playOne === '🦎' && playTwo === '📄') ||
    (playOne === '✂️' && playTwo === '🦎') ||
    (playOne === '🗿' && playTwo === '✂️')
  ) {
    playerOne++;
  } else {
    // player one lose!
    playerTwo++;
  }
};

const whoWin = (play: string[][]):void => {
  play.forEach((play) => points(play[0], play[1]));

  console.log(
    playerOne > playerTwo
      ? 'THe player 1 wins!'
      : playerTwo > playerOne
      ? 'The player 2 wins!'
      : 'Tie!'
  );
};

whoWin(plays[0]);
