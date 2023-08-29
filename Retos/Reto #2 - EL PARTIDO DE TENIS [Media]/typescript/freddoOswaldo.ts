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

const score = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
const LOVE = "Love";
const points = ["Love", "15", "30", "40"];
const DEUCE = "Deuce";
const ADVANTAGE = "Ventaja";
const WIN = "Ha ganado el";

interface MatchScore {
  P1: number;
  P2: number;
  finished: number;
}

type MatchScoreKey = keyof MatchScore;

function calculateMatchScore(point: string, matchScore: MatchScore) {
  const key = Object.keys(matchScore).find((p) => p === point) as MatchScoreKey;
  const notKey = Object.keys(matchScore).find(
    (p) => p !== point
  ) as MatchScoreKey;

  if (matchScore[key] === matchScore[notKey] && matchScore[key] === 3) {
    return DEUCE;
  }

  if (
    matchScore[key] > matchScore[notKey] &&
    matchScore[notKey] < 3 &&
    matchScore[key] === 4
  ) {
    matchScore.finished = 1;
    return `${WIN} ${key}`;
  }

  if (matchScore[key] === 4 && matchScore[notKey] === 3) {
    return `${ADVANTAGE} ${key}`;
  }

  if (matchScore[key] === 5 && matchScore[notKey] === 3) {
    matchScore.finished = 1;
    return `${WIN} ${key}`;
  }

  return `${points[matchScore.P1]} - ${points[matchScore.P2]}`;
}

function addPoints(point: string, matchScore: MatchScore) {
  const key = Object.keys(matchScore).find((p) => p === point) as MatchScoreKey;

  if (!key) {
    throw new Error("punto invalido");
  }

  matchScore[key] += 1;
}

function printMatchScore(scoreAfterAddPoint: string) {
  console.log(scoreAfterAddPoint);
}

function playTenis(score: string[] = []) {
  const matchScore: MatchScore = {
    P1: 0,
    P2: 0,
    finished: 0,
  };

  for (const point of score) {
    addPoints(point, matchScore);
    printMatchScore(calculateMatchScore(point, matchScore));
    if (!!matchScore.finished) break;
  }
}

playTenis(score);
