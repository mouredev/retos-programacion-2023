const model = {
  '🗿': ['🦎', '✂️'],
  '📄': ['🗿', '🖖'],
  '✂️': ['📄', '🦎'],
  '🦎': ['🖖', '📄'],
  '🖖': ['🗿', '✂️'],
}

let points_player1 = 0;
let points_player2 = 0;

function newGame(plays) {
  points_player1=0;
  points_player2=0;
  plays.forEach(playGame);
  if(points_player1===points_player2){
    return 'Tie';
  }else if(points_player1>points_player2){
    return 'Player 1';
  }else {
    return 'Player 2';
  }
}

function playGame([player1, player2]) {
  if (model[player1].indexOf(player2) > -1) {
    points_player1 += 1
  } else if (model[player2].indexOf(player1) > -1) {
    points_player2 += 1
  }
}

console.log(newGame([["🗿", "✂️"], ["✂️", "🗿"], ["📄", "✂️"]]))