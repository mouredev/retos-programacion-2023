const tennisMatch = (input) => {
  let points = gameScore(input);
  // console.log("points:", points);
  let tennisGame = tennisScore(points);
  // console.log("tennisGame: ", tennisGame);
  printGameScoreES(tennisGame);
  return points;
};

const gameScore = (input) => {
  // console.log("gameScore - input:", input);
  if (invalidInput(input)) {
    return [[-1, -1]];
  }
  let scores = [];
  input.forEach((player) => {
    let temp = [0, 0];
    if (scores.length != 0)
      temp = JSON.parse(JSON.stringify(scores[scores.length - 1]));
    if (player == "P1") temp[0] += 1;
    if (player == "P2") temp[1] += 1;
    scores.push(temp);
  });
  return scores;
};

const tennisScore = (gameScores) => {
  const scores = { 0: "love", 1: "15", 2: "30", 3: "40", 4: "50" };

  if (invalidScore(gameScores)) return ["invalid input"];

  return gameScores.map(([p1, p2]) => {
    let diff = Math.abs(p1 - p2);
    if ((p1 < 3 || p2 < 3) && diff <= 3)
      return [scores[String(p1)], scores[String(p2)]];
    else if (diff == 0) return ["deuce"];
    else if (diff == 1) return [`advantage ${p1 > p2 ? "P1" : "P2"}`];
    else if (p1 == 0 || p2 == 0 || diff > 1)
      return [`game ${p1 > p2 ? "P1" : "P2"}`];
    else console.log("I shall never be reached ;-)");
  });
};

const printGameScoreES = (tennisScore) => {
  console.log("\n\nJuego de Tennis\n===============\n\nP1  |  P2\n---------");
  if (JSON.stringify(tennisScore) == JSON.stringify(["invalid input"])) {
    console.log("Input inválido");
  } else {
    tennisScore.forEach(([p1, p2]) => {
      console.log(
        `${translateToSpanish(p1)}` +
          `${p2 ? "  |  " + translateToSpanish(p2) : ""}`
      );
    });
  }
};

const invalidInput = (input) => {
  if (input.length == 0) return true;

  return !input.every((elem) => elem == "P1" || elem == "P2");
};

const invalidScore = (scores) => {
  let [p1, p2] = scores[scores.length - 1];
  let diff = Math.abs(p1 - p2);

  if (diff == 2 || (diff == 4 && [p1, p2].includes(0))) return false;
  return true;
};

const translateToSpanish = (score) => {
  const spanishScore = { advantage: "ventaja", game: "ha ganado el" };

  if (!score) return false;

  let resp = null;
  for (let key in spanishScore) {
    if (score.match(key)) {
      resp = score.replaceAll(key, capitalize(spanishScore[key]));
    }
  }

  if (!resp) resp = capitalize(score);
  return resp;
};

const capitalize = (text) => text.slice(0, 1).toUpperCase() + text.slice(1);

// Tests types
// 1. completo: válido P1 tiene +2 que P1 después de 3 puntos
// 2. completo: válido, P2 llega a 3 puntos primero
// 3. input inválido, vacio
// 4. input inválido, input tiene información puntaje extra
// 5. input inválido, input tiene información puntaje extra
// 6. input inválido, input incompleto
// 7. input inválido, input incorrecto

const tests = {
  input: [
    ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"],
    ["P2", "P2", "P2", "P2"],
    [],
    ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P1"],
    ["P2", "P2", "P2", "P2", "P2"],
    ["P1", "P1", "P2", "P2"],
    ["P1", "A2", "p", "p2"],
  ],
  output: [
    [
      [1, 0],
      [2, 0],
      [2, 1],
      [2, 2],
      [3, 2],
      [3, 3],
      [4, 3],
      [5, 3],
    ],
    [
      [0, 1],
      [0, 2],
      [0, 3],
      [0, 4],
    ],
    [[-1, -1]],
    [
      [1, 0],
      [2, 0],
      [2, 1],
      [2, 2],
      [3, 2],
      [3, 3],
      [4, 3],
      [5, 3],
      [6, 3],
    ],
    [
      [0, 1],
      [0, 2],
      [0, 3],
      [0, 4],
      [0, 5],
    ],
    [
      [1, 0],
      [2, 0],
      [2, 1],
      [2, 2],
    ],
    [[-1, -1]],
  ],
};

let errors = 0;
tests.input.forEach((test, index) => {
  resp = tennisMatch(test);
  let expected = tests.output[index];
  if (JSON.stringify(resp) != JSON.stringify(expected)) {
    errors += 1;
    console.log("\n\noriginal: ", test);
    console.log(resp);
    console.log("expected: ", expected);
  }
});

console.log(
  `\n\nTests${errors != 0 ? " not " : " "}passed, ${errors} errors\n`
);
