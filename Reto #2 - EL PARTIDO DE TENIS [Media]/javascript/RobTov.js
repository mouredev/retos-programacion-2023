"use strict";

function tennisGame(sequence) {
  validateSequence(sequence);

  const points = { p1: 0, p2: 0 };
  console.log("P1   |    P2\n     |      ");

  sequence.forEach((p) => {
    p === "P1" ? (points.p1 += 1) : (points.p2 += 1);
    console.log(comparePoints(points));
  });
}

function validateSequence(sequence) {
  let p1Points = sequence.filter((s) => s === "P1").length;
  let p2Points = sequence.filter((s) => s === "P2").length;
  let p1Win = p1Points >= 4 && p1Points === p2Points + 2;
  let p2Win = p2Points >= 4 && p2Points === p1Points + 2;

  if (!Array.isArray(sequence)) {
    throw new Error("Los datos deben de estar dentro de un array.");
  }
  if (sequence.filter((s) => typeof s !== "string").length !== 0) {
    throw new Error("Todos los datos deben de ser de tipo string.");
  }
  if (p1Points + p2Points !== sequence.length) {
    throw new Error("Los datos solo pueden tener como valor P1 o P2.");
  }
  if (!(p1Win || p2Win)) {
    throw new Error("La secuencia es un partido sin ganador.");
  }
}

function comparePoints(points) {
  const scores = { p1: "Love", p2: "Love" };
  const scoreValues = ["Love", "15", "30", "40"];
  let out = "";

  if (points.p1 >= 3 || points.p2 >= 3) {
    if (points.p1 === points.p2 + 2) {
      out = "Ha ganado el P1";
    } else if (points.p1 >= 4 && points.p1 === points.p2 + 1) {
      out = "Ventaja de P1";
    } else if (points.p2 === points.p1 + 2) {
      out = "Ha ganado el P2";
    } else if (points.p2 >= 4 && points.p2 === points.p1 + 1) {
      out = "Ventaja de P2";
    } else if (points.p1 === points.p2) {
      out = "Deuce";
    } else {
      scores.p1 = scoreValues[points.p1];
      scores.p2 = scoreValues[points.p2];
      out = `${scores.p1}   |   ${scores.p2}`;
    }
  } else {
    scores.p1 = scoreValues[points.p1];
    scores.p2 = scoreValues[points.p2];
    out = `${scores.p1}   |   ${scores.p2}`;
  }

  return out;
}

const start = () => {
  tennisGame(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]);
};

start();
