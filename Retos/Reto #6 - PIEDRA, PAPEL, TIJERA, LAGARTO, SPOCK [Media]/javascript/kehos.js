/*
 * Reto #6 - Piedra, papel, tijera, lagarto, spock
 * Propuesta de solución realizada por Kehos
 * https://github.com/Kehos
 * 20/02/2023
 */

// Possible game moves IDs
const MOVES = {
  ROCK: 'Rock',
  PAPER: 'Paper',
  SCISSORS: 'Scissors',
  LIZARD: 'Lizard',
  SPOCK: 'Spock'
};

// Game moves index for evaluation
const MOVE_INDEX = {
  'Rock': 0,
  'Paper': 1,
  'Scissors': 2,
  'Lizard': 3,
  'Spock': 4
};

// Games moves mapping, setting which player wins depending on each players move
const MOVES_MAPPING = [
  [ 'T', 2, 1, 1, 2 ],
  [ 1, 'T', 2, 2, 1 ],
  [ 2, 1, 'T', 1, 2 ],
  [ 2, 1, 2, 'T', 1 ],
  [ 1, 2, 1, 2, 'T' ]
];

// Player score counter
var player1 = 0;
var player2 = 0;
const TIE = 'T';

function checkRound(move1, move2) {
  console.log('Jugador 1 juega: ' + move1 + ' | Jugador 2 juega: ' + move2);
  const result = MOVES_MAPPING[MOVE_INDEX[move1]][MOVE_INDEX[move2]];
  console.log(result === 'T' ? '-- Ronda empatada --\n' : '-- Ronda ganada por: Jugador ' + result + ' --\n');
  if (result !== TIE) {
    if (result === 1) {
      player1++;
    } else {
      player2++;
    }
  }
}

// Get player moves and eval each round
function evalGame(gameMoves) {
  console.log('\nROCK | PAPER | SCISSORS | LIZARD | SPOCK\nJugadas a evaluar:\n', gameMoves, '\n');
  player1 = 0;
  player2 = 0;
  gameMoves.forEach( game => checkRound(game[0], game[1]) );
  const gameResult = player1 === player2 ? 'Empate!' : player1 > player2 ? 'Gana jugador 1' : 'Gana jugador 2';
  console.log(gameResult + ' -> ' + player1 + '/' + player2);
}

const gameMoves1 = [
  [MOVES.ROCK, MOVES.SPOCK],
  [MOVES.PAPER, MOVES.PAPER],
  [MOVES.LIZARD, MOVES.SCISSORS],
  [MOVES.PAPER, MOVES.SPOCK]
];
evalGame(gameMoves1);

console.log('\n----------\n');

const gameMoves2 = [
  [MOVES.SPOCK, MOVES.SPOCK],
  [MOVES.PAPER, MOVES.SCISSORS],
  [MOVES.ROCK, MOVES.SCISSORS],
  [MOVES.LIZARD, MOVES.SPOCK],
  [MOVES.LIZARD, MOVES.ROCK],
  [MOVES.SCISSORS, MOVES.SPOCK],
  [MOVES.PAPER, MOVES.SCISSORS],
  [MOVES.LIZARD, MOVES.PAPER],
  [MOVES.SPOCK, MOVES.SCISSORS],
];
evalGame(gameMoves2);

