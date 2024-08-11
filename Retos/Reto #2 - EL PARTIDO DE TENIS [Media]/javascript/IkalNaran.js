const gameTennis = (secuencia) => {
  const pointGame = [15, 30, 40, 41, 42, 43, 44];

  let pointP1 = 0;
  let pointP2 = 0;
  let gameWinP1 = ["Love"];
  let gameWinP2 = ["Love"];
  let win1 = 1;
  let win2 = 1;

  for (element of secuencia) {
    (element == 'P1') ? gameWinP1.push(pointGame[pointP1++]) : (element == 'P2') ? gameWinP2.push(pointGame[pointP2++]) : "";
    let player1 = gameWinP1[pointP1];
    let player2 = gameWinP2[pointP2];
    let playerMayor = player1 >= 40 && player2 >= 40;

    try {
      if ((player1 == player2) && playerMayor) {
        console.log('Douce');
        win1 = 1;
        win2 = 1;
      } else if (player1 > 40 && player2 <= 30 || player1 <= 30 && player2 >= 40) {
        console.log(`Ha ganado ${element}`);
        break;
      } else if (win1 >= 2 || win2 >= 2) {
        console.log(`Ha ganado ${element}`);
        break;
      } else if (pointP1 > pointP2 && playerMayor) {
        console.log(`Ventaja ${element}`);
        win1++;
      } else if ((player1 < player2) && playerMayor) {
        console.log(`Ventaja ${element}`);
        win2++;
      } else console.log(`${player1} - ${player2}`);

    } catch (error) {
      console.log(error);
    }
  }

}

let secuencia1 = ['P2', 'P1', 'P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2', 'P2', 'P2'];
let secuencia = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'];
gameTennis(secuencia); 
