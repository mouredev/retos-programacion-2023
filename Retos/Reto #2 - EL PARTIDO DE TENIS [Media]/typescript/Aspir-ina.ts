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

enum Score {
  Love,
  Fifteen,
  Thirty,
  Forty,
  Deuce,
  Advantage,
  Winner
}

class Player {
  private _score: number = Score.Love;

  set score(score: number) {
    this._score = score;
  }

  get score(): number {
    return this._score;
  }

  get isWinner(): boolean {
    return this._score === Score.Winner;
  }
}

const game = (match: string[]) => {
  const scores: string[] = ['Love', '15', '30', '40', 'Deuce', 'Advantage', 'Winner'];
  const player1: Player = new Player();
  const player2: Player = new Player();
  let gameWinner: boolean = false;

  match.every((matchPoint: string) => {
    (matchPoint === 'P1')
      ? updatePlayerScore(player1, player2)
      : updatePlayerScore(player2, player1);

    console.log('Player 1:', scores[player1.score], ' <-> Player2:', scores[player2.score]);

    const currentPlayer = matchPoint === 'P1' ? player1 : player2;
    gameWinner = currentPlayer.isWinner;

    if (gameWinner)
      console.log(`Player ${matchPoint} wins`);

    return !gameWinner;
  });

  if (!gameWinner)
    console.log('No player has won');
}

const updatePlayerScore = (currentPlayer: Player, nextPlayer: Player): void => {
  switch (currentPlayer.score) {
    case Score.Love:
    case Score.Fifteen:
    case Score.Thirty:
    case Score.Advantage:
      currentPlayer.score++;
      break;
    case Score.Forty:
      currentPlayer.score++;

      const currentPlayerWins = currentPlayer.score - 2 >= nextPlayer.score;
      const playersDeuce = currentPlayer.score === nextPlayer.score;

      if (currentPlayerWins)
        currentPlayer.score = Score.Winner;
      else if (playersDeuce) {
        currentPlayer.score = Score.Deuce;
        nextPlayer.score = Score.Deuce;
      } else currentPlayer.score = Score.Advantage;
      break;
    case Score.Deuce:
      currentPlayer.score = Score.Advantage;
      break;
  }
}

const match: string[] = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'];// Reto match
const match2: string[] = ['P1', 'P1'];// Ningún jugador ha ganado
const match3: string[] = ['P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P1'];// Al 4 item debería parar el loop porque se decide el ganador. Llegar a 40 y tener ventaja de 2
game(match);
game(match2);
game(match3);