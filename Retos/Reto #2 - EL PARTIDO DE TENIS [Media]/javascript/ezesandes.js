/**
 *
 * @param {Array} secuences
 */
function juegoDeTenis(secuences) {
  let scoreP1 = 0,
    scoreP2 = 0;

  const dic = {
    0: 'Love',
    1: 15,
    2: 30,
    3: 40,
    4: 'Deuce',
  };

  for (const player of secuences) {
    player === 'P1' ? scoreP1++ : scoreP2++;

    if (Math.abs(scoreP1 - scoreP2) >= 2) {
      if (scoreP1 > 3 || scoreP2 > 3) {
        console.log(`Ha ganado ${scoreP1 > scoreP2 ? 'P1' : 'P2'}`);
        return;
      }
    }

    if ((scoreP1 > 3 || scoreP2 > 3) && Math.abs(scoreP1 - scoreP2) === 1) {
      console.log(`Ventaja ${scoreP1 > scoreP2 ? `P1` : `P2`}`);
      continue;
    }

    if (scoreP1 >= 3 && scoreP2 >= 3) {
      console.log(dic[4]);
      continue;
    }

    console.log(`${dic[scoreP1]} - ${dic[scoreP2]}`);
  }
}

juegoDeTenis(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
// juegoDeTenis(['P1', 'P1', 'P1', 'P1']);
// juegoDeTenis(['P2', 'P2', 'P2', 'P2']);
// juegoDeTenis(['P2', 'P1', 'P2', 'P1', 'P1', 'P2', 'P1', 'P1']); // Gana P1
// juegoDeTenis(['P2', 'P1', 'P2', 'P1', 'P2', 'P2']); // Gana P2
// juegoDeTenis(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2', 'P2']); //gana P2
