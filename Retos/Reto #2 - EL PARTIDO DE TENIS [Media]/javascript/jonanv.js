function tennisGame(points) {
  let score = ['Love', 15, 30, 40];
  let match = {
    P1: 0,
    P2: 0
  }

  console.log(score[match.P1] + ' - ' + score[match.P2]);
  for (let index = 0; index < points.length; index++) {

    (points[index] === 'P1') ? match.P1 += 1 : match.P2 += 1;

    if (score[match.P1] === 40 && score[match.P2] === 40) {
      console.log('Douce');
    } else if (match.P1 >= 4 || match.P2 >= 4) {
      console.log(`Ventaja ${match.P1 > match.P2 ? 'P1' : 'P2'}`);
    } else {
      console.log(score[match.P1] + ' - ' + score[match.P2]);
    }

    if (match.P1 > 3 ||
      match.P2 > 3 &&
      Math.abs(match.P1 - match.P2) === 2) {
      index = points.length;
    }
  }
  console.log(`Ha ganado el ${match.P1 > match.P2 ? 'P1' : 'P2'} \n`);
}

tennisGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1', 'P1', 'P1', 'P1', 'P2']);
tennisGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
tennisGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1', 'P2', 'P1']);
tennisGame(['P1', 'P1', 'P1', 'P1', 'P1', 'P1']);
tennisGame(['P1', 'P1']);
tennisGame(['P2', 'P2', 'P1', 'P1', 'P2', 'P1', 'P2', 'P2', 'P1', 'P2']);