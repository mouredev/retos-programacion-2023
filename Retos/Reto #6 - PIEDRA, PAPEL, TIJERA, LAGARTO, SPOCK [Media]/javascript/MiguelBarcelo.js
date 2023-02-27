const rockPaperScissorsLizardSpock = (game) => {

  const Defeats = {
    "🗿": [ "🦎", "✂️" ],
    "📄": [ "🗿", "🖖" ],
    "✂️": [ "📄", "🦎" ],
    "🦎": [ "🖖", "📄" ],
    "🖖": [ "🗿", "✂️" ]
  }

  const Results = {
    P1: 'Player 1',
    P2: 'Player 2',
    TIE: 'Tie'
  }

  const score = game.reduce((score, [p1, p2]) => {
    p1 === p2 
      ? (score[0]++, score[1]++)
      : Defeats[p1].includes(p2) ? score[0]++ : score[1]++;
    
    return score;
  }, [0 , 0]);

  return score[0] == score[1]
    ? Results.TIE 
    : score[0] > score[1] ? Results.P1 : Results.P2;
}
