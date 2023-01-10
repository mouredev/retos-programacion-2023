/*
 * Reto #2 - El partido de tenis
 * Propuesta de solución realizada por Kehos
 * https://github.com/Kehos
 * 10/01/2023
 */

// Test array
const game = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2', 'P2'];

// Player scores
const SCORES = {
  LOVE: 'Love',
  FIFTEEN: '15',
  THIRTY: '30',
  FORTY: '40',
  ADVANTAGE: 'Ventaja',
  DEUCE: 'Deuce',
  VICTORY: 'Victoria'
};
const PLAYER_1 = 'P1';
const PLAYER_2 = 'P2';

// Player score count
const PLAYER_SCORE = {
  P1: SCORES.LOVE,
  P2: SCORES.LOVE
};

// Game end control
let gameEnd = false;

// Get which player scores points and resolve score
function score(player) {
  let resultText = '';
  switch(PLAYER_SCORE[player]) {
    case SCORES.LOVE:
      PLAYER_SCORE[player] = SCORES.FIFTEEN;
      break;
    case SCORES.FIFTEEN:
      PLAYER_SCORE[player] = SCORES.THIRTY;
      break;
    case SCORES.THIRTY:
      PLAYER_SCORE[player] = SCORES.FORTY;
      if (PLAYER_SCORE.P1 === PLAYER_SCORE.P2) {
        PLAYER_SCORE.P1 = SCORES.DEUCE;
        PLAYER_SCORE.P2 = SCORES.DEUCE;
        resultText = SCORES.DEUCE;
      }
      break;
    case SCORES.FORTY:
      if ((player === PLAYER_1 && PLAYER_SCORE[PLAYER_2] === SCORES.ADVANTAGE) ||
        (player === PLAYER_2 && PLAYER_SCORE[PLAYER_1] === SCORES.ADVANTAGE)) {
        PLAYER_SCORE.P1 = SCORES.DEUCE;
        PLAYER_SCORE.P2 = SCORES.DEUCE;
        resultText = SCORES.DEUCE;
      } else {
        PLAYER_SCORE[player] = SCORES.VICTORY;
        resultText = PLAYER_SCORE[player] + ' ' + player;
        gameEnd = true;
      }
      break;
    case SCORES.DEUCE:
      PLAYER_SCORE[player] = SCORES.ADVANTAGE;
      if (player === PLAYER_1) {
        PLAYER_SCORE[PLAYER_2] = SCORES.FORTY;
      } else {
        PLAYER_SCORE[PLAYER_1] = SCORES.FORTY;
      }
      resultText = PLAYER_SCORE[player] + ' ' + player;
      break;
    case SCORES.ADVANTAGE:
      PLAYER_SCORE[player] = SCORES.VICTORY;
      resultText = PLAYER_SCORE[player] + ' ' + player;
      gameEnd = true;
      break;
  }
  console.log(resultText !== '' ? resultText : PLAYER_SCORE.P1 + ' - ' + PLAYER_SCORE.P2);
}

function evalGame() {
  game.forEach(
    player => {
      if (!gameEnd) {
        score(player);
      }
    }
  );
}

console.log('Game score: ' + game.join(', ') + '\n');
evalGame();
