'use strict';

const BEATS = {
  '🗿': new Set(['✂️', '🦎']),
  '📄': new Set(['🗿', '🖖']),
  '✂️': new Set(['📄', '🦎']),
  '🦎': new Set(['📄', '🖖']),
  '🖖': new Set(['🗿', '✂️'])
};

function play(games) {
  let player1 = 0;
  let player2 = 0;
  for (const [first, second] of games) {
    if (!BEATS[first] || !BEATS[second]) throw new Error('Jugada no válida');
    if (first === second) continue;
    if (BEATS[first].has(second)) player1++;
    else player2++;
  }
  return player1 === player2 ? 'Tie' : player1 > player2 ? 'Player 1' : 'Player 2';
}

module.exports = { play };

if (require.main === module) console.log(play([['🗿', '✂️'], ['✂️', '🗿'], ['📄', '✂️']]));
