
const prompt = require("prompt-sync")();

const emojis = { car1: "🚙", car2: "🚗", tree: "🌲", end: "🏁", crash: "💥" };
let raceDistance = 5;
let userBet = "azul";
let track1 = [emojis.end],
  track2 = [emojis.end];

//preguntar la distancia de la carrera
function userSelection() {
  raceDistance = prompt(
    "Que distancia quieres que tenga la pista (min.5 - max.30)? : "
  );

  while (raceDistance > 30 || raceDistance < 5 || isNaN(raceDistance)) {
    raceDistance = prompt(
      "La distancia tiene que ser entre min. 5 - max.30)? : "
    );
  }

  //preguntar por que coche quiere apostar
  userBet = prompt("A que coche quieres apostar el 'azul' o el 'rojo'? : ");
  userBet = userBet.toLowerCase();

  while (userBet !== "azul" && userBet !== "rojo") {
    userBet = prompt("Sólo puedes seleccionar coche 'azul' o coche 'rojo'? : ");
    userBet = userBet.toLowerCase();
  }
  generateTrack();
}
//generar pistas con de 1 a 3 arboles aleatorios
function generateTrack() {
  const numberOfTrees = getRandomInt(4, 1);

  for (let i = 0; i < raceDistance; i++) {
    track1.push("_");
    track2.push("_");
  }

  for (i = 0; i < numberOfTrees; i++) {
    let randomPos1 = getRandomInt(raceDistance, 1);
    let randomPos2 = getRandomInt(raceDistance, 1);

    while (track1[randomPos1] === emojis.tree)
      randomPos1 = getRandomInt(raceDistance, 1);
    while (track2[randomPos2] === emojis.tree)
      randomPos2 = getRandomInt(raceDistance, 1);

    track1[randomPos1] = emojis.tree;
    track2[randomPos2] = emojis.tree;
  }

  track1.push(emojis.car1);
  track2.push(emojis.car2);
  showRace();
  countdown();
}
//mostrar arranque de la carrera
function countdown() {
  let c = 3;
  let countdownIdInterval = setInterval(() => {
    if (c == 0) {
      console.log("START");
      clearInterval(countdownIdInterval);
      raceStart();
    } else console.log(c);
    c--;
  }, 1000);
}

//generar turnos y movimientos aleatorio
function raceStart() {
  let randomMov1 = 1;
  let randomMov2 = 1;
  let ind1 = 0;
  let ind2 = 0;
  showRace();
  raceIdInt = setInterval(() => {
    randomMov1 = getRandomInt(4, 1);
    randomMov2 = getRandomInt(4, 1);
    
    if (randomMov1 > track1.length) randomMov1 = track1.length;
    
    ind1 = track1.length - (randomMov1 + 1);

    if ( randomMov2 > track2.length) randomMov2 = track2.length;
    
    ind2 = track2.length - (randomMov2 + 1);


    (track1[ind1] === emojis.tree) 
    ? track1.splice(ind1, randomMov1, emojis.crash)
    : track1.splice(ind1, randomMov1);
    

    (track2[ind2] === emojis.tree)
    ? track2.splice(ind2, randomMov2, emojis.crash)
    : track2.splice(ind2, randomMov2);

    showRace();

    if (track1.length <= 1 || track2.length <= 1) {
      showResult();
      clearInterval(raceIdInt);
    }
  }, 1000);
}

//gestionar choque

//mostrar ganador y resultado de la apuesta
function showResult() {
  //gestionar empate
  const winner =
    track1.length === 1 ? (track2.length === 1 ? "both" : "azul") : "rojo";
  const betResult = winner === userBet || winner === "both" ? "win" : "lost";
  console.log(`FINISH! ${winner.toUpperCase()} WINS!! `);
  console.log(`You ${betResult} your bet`);
}

function showRace() {
  console.clear();
  console.log(track1.join(""));
  console.log(track2.join(""));
}

function getRandomInt(max, min) {
  return Math.floor(Math.random() * (max - min) + min); // The maximum is exclusive and the minimum is inclusive
}

userSelection();
