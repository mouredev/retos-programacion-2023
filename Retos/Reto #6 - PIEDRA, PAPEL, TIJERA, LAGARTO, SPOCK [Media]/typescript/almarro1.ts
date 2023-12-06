const MODEL: Record<string, string[]> = {
  '🗿': ['🦎', '✂️'],
  '📄': ['🗿', '🖖'],
  '✂️': ['📄', '🦎'],
  '🦎': ['🖖', '📄'],
  '🖖': ['🗿', '✂️'],
}

let POINTS_PLAYER1 = 0;
let POINTS_PLAYER2 = 0;

function newGame(plays: string[][]): string {
  POINTS_PLAYER1 = 0;
  POINTS_PLAYER2 = 0;
  plays.forEach(playGame);
  if (POINTS_PLAYER1 === POINTS_PLAYER2) {
    return 'Tie';
  } else if (POINTS_PLAYER1 > POINTS_PLAYER2) {
    return 'Player 1';
  } else {
    return 'Player 2';
  }
}

function playGame([player1, player2]: string[]): void {
  if (MODEL[player1].indexOf(player2) > -1) {
    POINTS_PLAYER1 += 1
  } else if (MODEL[player2].indexOf(player1) > -1) {
    POINTS_PLAYER2 += 1
  }
}

console.log(newGame([["🗿", "✂️"], ["✂️", "🗿"], ["📄", "✂️"]]))