const puntaje = ["Love", 15, 30, 40];

function checkMatch(puntos) {
  let puntajes = {
    P1: 0,
    P2: 0,
  };

  for (const element of puntos) {
    puntajes[element]++;

    if (puntajes.P1 <= 3 && puntajes.P2 <= 3) {
      console.log(
        puntaje[puntajes.P1] + " - " + puntaje[puntajes.P2] === "40 - 40"
          ? "Deuce"
          : ""
      );
    } else if (puntajes.P1 === puntajes.P2) {
      console.log("Deuce");
    } else {
      const ventaja = puntajes.P1 > puntajes.P2 ? "P1" : "P2";

      if (Math.abs(puntajes.P1 - puntajes.P2) >= 2) {
        console.log("Ganó el " + ventaja);
        return;
      } else if (ventaja) {
        console.log("Ventaja el " + ventaja);
      }
    }
  }
}

checkMatch([
  "P1",
  "P1",
  "P1",
  "P2",
  "P2",
  "P2",
  "P1",
  "P2",
  "P2",
  "P1",
  "P1",
  "P2",
  "P2",
  "P1",
  "P1",
  "P1",
]);
