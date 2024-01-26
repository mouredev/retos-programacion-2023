const player1 = 'P1';
const player2 = 'P2';

const score = ['love', '15', '30', '40', 'Deuce', 'Advantage', 'Win'];

let player1Score = score[0];
let player2Score = score[0];

let p1points = 0;
let p2points = 0;
function getScore(player) {

  if (player === player1) {
    player1Score = score[p1points + 1];
    p1points += 1;
    
  }
  if (player === player2) {
    player2Score = score[p2points + 1];
    p2points += 1;
  }

  if (player1Score === score[3] && player2Score === score[3]) {
    player1Score = score[4];
    player2Score = score[4];
  }
  return console.log(`${player1} - ${player2} 
${player1Score}: ${player2Score}`);
}

getScore(player1);
getScore(player1);
getScore(player2);
getScore(player2);
getScore(player1);
getScore(player2);
getScore(player1);
getScore(player1);
getScore(player1);
