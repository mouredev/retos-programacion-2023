let P1 = 0;
let P2 = 0;
let secuencia = ["P2", "P2", "P1", "P1", "P1", "P2", "P1", "P1"];
let puntuacion = { 0: "Love", 1: 15, 2: 30, 3: 40 };

function playTennis(n) {
  while (P1 < 5 || P2 < 5) {
    if (secuencia[n] == "P1") {
      P1++;
    } else if (secuencia[n] == "P2") {
      P2++;
    } 
    if (P1 > 2 && P2 > 2 && P1 == P2) {
      return "deuce";
    }
    if ((P1 == 4) | (P2 == 4)) {
      return `${P1 > P2 ? "P1" : "P2"} tiene la ventaja`;
    }
    if ((P1 == 5) | (P2 == 5)) {
      return `${P1 > P2 ? "P1" : "P2"} Gana`;
    }
    if ((P1 > 5) | (P2 > 5)) {
      return "El juego ha finalizado";
    } else {
      return puntuacion[P1] + "-" + puntuacion[P2];
    }
  }
}
function startGame() {
  if (secuencia.every((element) => element == "P1" || element == "P2")) {
    secuencia.forEach((element, i) => {
      console.log(playTennis(i));
    });
  }else{
    return "Solo se permiten 2 jugadores"
  }
}
startGame();
