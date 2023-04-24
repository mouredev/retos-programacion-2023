'use strict';

const tenisGame = (game) => {
  'use strict';

  const POINTS = {
    '0': 'Love',
    '1': '15',
    '2': '30',
    '3': '40',
    DEUCE: 'Deuce',
    VENTAJA: 'Ventaja',
    GANADO: 'Ha ganado el'
  }

  const playersHaveThreePoints = (player, oppositePlayer) =>
    player.points == oppositePlayer.points && player.points == 3
  
  const isPlayerUpInAllSet = (player, oppositePlayer) =>
    player.points > oppositePlayer.points && player.extraPoints == 1
    
  const playersDontHaveExtraPoints = (player, oppositePlayer) =>
    player.extraPoints == 0 && oppositePlayer.extraPoints == 0
  
  const setPoint = player => {
    'use strict';

    if (player.points <= 2) {
      player.points = player.points + 1;
      return;
    }

    if (player.points == 3) {
      player.extraPoints = player.extraPoints + 1;
      return;
    }
  }

  const createScore = (player, { score, game }) => {

    const oppositePlayer = score[player.opposite];

    if (playersHaveThreePoints(player, oppositePlayer) && playersDontHaveExtraPoints(player, oppositePlayer)) {
      game.push(POINTS.DEUCE)
      return;
    }

    if (isPlayerUpInAllSet(player, oppositePlayer) || (playersHaveThreePoints(player, oppositePlayer) && player.advantage)) {
        game.push(`${POINTS.GANADO} ${player.name}`)
        return;
    }

    if (playersHaveThreePoints(player, oppositePlayer)) {
      game.push(`${POINTS.VENTAJA} ${player.name}`)
      player.advantage = true;
      oppositePlayer.advantage = false;
      return;
    }

    game.push(`${POINTS[score.P1.points]} - ${POINTS[score.P2.points]}`)
    return;
  }

  const initialState = { 
    score: { 
      P1: { points: 0, extraPoints: 0, name: 'P1', opposite: 'P2', advantage: false }, 
      P2: { points: 0, extraPoints: 0, name: 'P2', opposite: 'P1', advantage: false } 
    }, 
    game: [] 
  }

  return game.reduce((acc, player) => {
      setPoint(acc.score[player])
      createScore(acc.score[player], acc);

      return acc;
  }, initialState).game.join('\n');
}