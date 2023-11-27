const MAX_TREES = 3;
const TREE_LIKEHOOD = 0.3;
const MAX_MOVE = 3;
const SIMULATION_STEP_MS = 1000;
const TARGET = "🏁";
const CAR1 = "🚙";
const CAR2 = "🚗";
const TREE = "🌲";
const CRASH = "💥";
const ROAD = "_";

function waitNextStep() {
  return new Promise(resolve => setTimeout(resolve,
                                SIMULATION_STEP_MS));
}

function showRaceStatus(header, road1, road2) {
  console.log(header);
  console.log(road1.join(""));
  console.log(road2.join(""));
}

function generateRoad(car, roadSize) {
  let road = [];
  let numTrees = 0;

  road.push(TARGET);

  for(let i = 0 ; i < roadSize ; i++) {
    if (numTrees < MAX_TREES) {
      let p = Math.random();
      if (p < TREE_LIKEHOOD) {
        road.push(TREE);
        numTrees++;
      }
      else {
        road.push(ROAD);
      }
      continue;
    }

    road.push(ROAD);
  }

  road.push(car);

  return road;
}

async function runSimulation(road1, road2) {
  let raceFinish = false;
  let car1Crash = false;
  let car2Crash = false;

  while (!raceFinish) {
    await waitNextStep();

    let car1Move = Math.floor(1 + Math.random() * (MAX_MOVE - 1));
    let car2Move = Math.floor(1 + Math.random() * (MAX_MOVE - 1));
    let car1Index = road1.indexOf(CAR1);
    if (car1Index == -1)
      car1Index = road1.indexOf(CRASH);
    let car2Index = road2.indexOf(CAR2);
    if (car2Index == -1)
      car2Index = road2.indexOf(CRASH);
    let newCar1Index = ((car1Index - car1Move) < 0) ? 0 : (car1Index - car1Move);
    let newCar2Index = ((car2Index - car2Move) < 0) ? 0 : (car2Index - car2Move);

    if (!car1Crash) {
      car1Crash = (road1[newCar1Index] == TREE);
      road1[car1Index] = ROAD;
      road1[newCar1Index] = (car1Crash ? CRASH : CAR1);
    } else {
      car1Crash = false;
      newCar1Index = car1Index;
    }

    if (!car2Crash) {
      car2Crash = (road2[newCar2Index] == TREE);
      road2[car2Index] = ROAD;
      road2[newCar2Index] = (car2Crash ? CRASH : CAR2);
    } else {
      car2Crash = false;
      newCar2Index = car2Index;
    }

    showRaceStatus("Current", road1, road2);

    if ((!car1Crash && newCar1Index == 0) || (!car2Crash && newCar2Index == 0))
      raceFinish = true;
  }

  showRaceStatus("Final", road1, road2);

  if (road1[0] == CAR1 && road2[0] == CAR2) {
    console.log("Race: Draw");
  } else {
    if (road1[0] == CAR1) {
      console.log("Race: Car1 wins");
    } else {
      console.log("Race: Car2 wins");
    }
  }
}

const roadSize = 10;
let road1 = generateRoad(CAR1, roadSize);
let road2 = generateRoad(CAR2, roadSize);

showRaceStatus("Initial state", road1, road2);
runSimulation(road1, road2);
