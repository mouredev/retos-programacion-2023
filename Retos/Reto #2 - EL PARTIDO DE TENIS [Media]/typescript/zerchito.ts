/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

function resumeMatch(matchPlays:string[]): void {
  const players = {
    P1: 0,
    P2: 0
  }
  matchPlays.forEach(play => {
    players[play]++;
    // a partir de 3 puntos los empates son deuce
    if (players.P1 < 3 && players.P2 < 3 && !(players.P1 + players.P2 === 6) ) {
      console.log(`${transformScore(players.P1)} - ${transformScore(players.P2)}`);
    } else{
      if (players.P1 === players.P2) {
        console.log('Deuce');
      }
      if (Math.abs(players.P1 - players.P2) === 1){
        console.log(`Ventaja ${play}`);
      } else {
        console.log(`Ha ganado el ${play}`);
      }
    }
  })
}

function transformScore (score: number): string {
  switch(score){
    case 0: return 'Love';
    case 1: return '15'; 
    case 2: return '30';
    case 3: return '40';
    default: return `${score}`;
  }
}

resumeMatch(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);