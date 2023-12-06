

const gamePSLS = ( plays ) => {

  const scenarios = {

      "🗿": ["✂️", "🦎"],
      "📄": ["🗿", "🖖"],
      "✂️": ["📄", "🦎"],
      "🦎": ["📄", "🖖"],
      "🖖": ["🗿", "✂️"],
  }

  //Saving our counters
  let playerOne = 0;
  let playerTwo = 0;

  for( const play of plays  ) {

    const playerOnePlay = play[0]
    const playerTwoPlay = play[1]

    if( scenarios[playerOnePlay].includes(playerTwoPlay) ) {

      playerOne++

    }else {
      
      playerTwo++
    }
  }

  return playerOne === playerTwo ? "Tie"
                                 : playerOne > playerTwo
                                 ? "Player 1 won! 🙂 "
                                 : "Player 2 won! 🙂 "
}

console.log( gamePSLS([

  ["🗿", "✂️"],
    ["🖖", "🦎"],
    ["📄", "🗿"],

]))