const puntos = {0 : 'love', 1 : '15', 2 : '30', 3 : '40', 4 : 'Ventaja', 5 : 'Gana!'};
const marcador = [0, 0];

function setMarcador(player) {
  let p = (player=='P1') ? 0 : 1;
  let o = (player=='P2') ? 0 : 1;
  marcador[p]++;
  if (marcador[p] == 4 && marcador[o] < 3) {
    marcador[p]++;
  }
  if (marcador[p] == 4 && marcador[o] == 4) {
    marcador[p]=3;
    marcador[o]=3;
  }
  if (marcador[0] == 3 && marcador[1] == 3) {
    console.log('Deuce');
  }
  else {
    console.log(puntos[marcador[0]]+' | '+puntos[marcador[1]]);
  }
}

function procesarTantosJugardor(tantos) {
  marcador[0] = 0;
  marcador[1] = 0;
  for (let x = 0; x < tantos.length; x++) {
    setMarcador(tantos[x]);
  }
}

console.log('Juego 1');
tantosJugador = ['P1', 'P1', 'P2', 'P1', 'P1'];
procesarTantosJugardor(tantosJugador);
console.log('Juego 2');
tantosJugador = ['P1', 'P2', 'P2', 'P2', 'P2'];
procesarTantosJugardor(tantosJugador);
console.log('Juego 3');
tantosJugador = ['P1', 'P2', 'P1', 'P2', 'P2', 'P1', 'P1', 'P2', 'P2', 'P2'];
procesarTantosJugardor(tantosJugador);
