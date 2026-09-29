'use strict';

function tennisGame(points) {
  const score = { P1: 0, P2: 0 };
  const names = ['Love', '15', '30', '40'];
  const history = [];

  for (const player of points) {
    if (!(player in score)) throw new Error(`Jugador no válido: ${player}`);
    if (Math.abs(score.P1 - score.P2) >= 2 && Math.max(score.P1, score.P2) >= 4) {
      throw new Error('El juego ya había terminado');
    }

    score[player]++;
    if (score.P1 >= 4 || score.P2 >= 4) {
      const difference = score.P1 - score.P2;
      if (Math.abs(difference) >= 2) history.push(`Ha ganado el ${difference > 0 ? 'P1' : 'P2'}`);
      else if (difference === 0) history.push('Deuce');
      else history.push(`Ventaja ${difference > 0 ? 'P1' : 'P2'}`);
    } else if (score.P1 === 3 && score.P2 === 3) {
      history.push('Deuce');
    } else {
      history.push(`${names[score.P1]} - ${names[score.P2]}`);
    }
  }

  return history;
}

module.exports = { tennisGame };

if (require.main === module) {
  tennisGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']).forEach(line => console.log(line));
}
