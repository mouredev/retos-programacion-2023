/*
 Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 gane cada punto del juego.
 
 - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
   15 - Love
   30 - Love
   30 - 15
   30 - 30
   40 - 30
   Deuce
   Ventaja P1
   Ha ganado el P1
 - Si quieres, puedes controlar errores en la entrada de datos.   
 - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

// SOLUTION:
const punctuation = {
  0: "love",
  1: 15,
  2: 30,
  3: 40,
  4: 50,
  5: 60,
};

const players = {
  P1: 0,
  P2: 0,
};

const playingTennis = (points) => {
  points.forEach((player) => {
    if (player === "P1" || player === "P2") {
      players[player]++;
    };

    const data = `${punctuation[players.P1]} - ${punctuation[players.P2]}`
    console.log(data); 
    if (punctuation[players.P1] > punctuation[players.P2] && punctuation[players.P1] >= 50 && punctuation[players.P1] < 60) {
      console.log("advantage P1");
    } else if (punctuation[players.P2] > punctuation[players.P1] && punctuation[players.P2] >= 50 && punctuation[players.P2] < 60) {
      console.log("advantage P2");
    }
    if (punctuation[players.P1] === punctuation[players.P2]) {
      console.log("Deuce");
    }
  });

  console.log(`--- FINAL SCORE: ${punctuation[players.P1]} - ${punctuation[players.P2]}`)
  if (players.P1 > players.P2) {
    console.log("P1 IS THE WINNER");
  } else {
    console.log("P2 IS THE WINNER");
  }
};

playingTennis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]);
