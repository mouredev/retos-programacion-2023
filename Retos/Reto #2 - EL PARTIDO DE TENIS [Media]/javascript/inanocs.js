const POINTS = ["Love", "15", "30", "40"];

const TIE = "Deuce";
const AD = "AD to %player%";
const WINNER = "%player% win the game";
const POINTS_DIFFERENCE_MESSAGE = [TIE, AD, WINNER];

const UNKNOWN_PLAYER_ERROR = "Unknown player, available players: P1,P2";

const playMatch = (results = []) => {
  const players = {
    P1: { score: 0, rival: "P2" },
    P2: { score: 0, rival: "P1" },
  };

  const updateScoreMessage = (player) => {
    const { score: playerPoints, rival } = players[player];
    const { score: rivalPoints } = players[rival];

    const pointsDifference = playerPoints - rivalPoints;
    if (rivalPoints >= 3 && playerPoints >= 3) {
      const message = POINTS_DIFFERENCE_MESSAGE[pointsDifference];
      return message?.replace("%player%", player);
    }
    if (playerPoints === 4) {
      return POINTS_DIFFERENCE_MESSAGE[2].replace("%player%", player);
    } else {
      return `${POINTS[players.P1.score]} - ${POINTS[players.P2.score]}`;
    }
  };
  const matchResume = [];
  for (let playerPoint of results) {
    const player = players[playerPoint.toUpperCase()];
    if (!player) throw new Error(UNKNOWN_PLAYER_ERROR);
    player.score += 1;
    const message = updateScoreMessage(playerPoint);
    matchResume.push(message);
    if (message.includes("win")) break;
  }
  return matchResume;
};

const testSamples = [
  {
    testName: "P1 should win",
    input: ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P1"],
    expectedOutput: [
      "15 - Love",
      "30 - Love",
      "30 - 15",
      "30 - 30",
      "40 - 30",
      "Deuce",
      "AD to P1",
      "P1 win the game",
    ],
  },
  {
    testName: "P2 should win",
    input: ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"],
    expectedOutput: [
      "15 - Love",
      "30 - Love",
      "30 - 15",
      "30 - 30",
      "40 - 30",
      "Deuce",
      "AD to P1",
      "Deuce",
      "AD to P2",
      "P2 win the game",
    ],
  },
  {
    testName: "P1 should win without ties",
    input: ["P1", "P1", "P2", "P2", "P1", "P1"],
    expectedOutput: [
      "15 - Love",
      "30 - Love",
      "30 - 15",
      "30 - 30",
      "40 - 30",
      "P1 win the game",
    ],
  },
  {
    testName: "P2 should win without ties",
    input: ["P2", "P1", "P1", "P2", "P2", "P2"],
    expectedOutput: [
      "Love - 15",
      "15 - 15",
      "30 - 15",
      "30 - 30",
      "30 - 40",
      "P2 win the game",
    ],
  },
  {
    testName: "Should raise exception, unknown player",
    input: ["P2", "P1", "P3", "P2", "P2", "P2"],
    expectedOutput: UNKNOWN_PLAYER_ERROR,
  },
];
const runTests = () => {
  const passedTests = testSamples.filter((test) => {
    const { testName, input, expectedOutput } = test;
    let output = "";
    try {
      output = playMatch(input);
    } catch (e) {
      output = e.message;
    }
    const IS_EXPECTED_RESULT =
      JSON.stringify(output) === JSON.stringify(expectedOutput);
    const LOG_TEST_NAME = `Test ${testName}`;
    const LOG_TEST_RESULT = IS_EXPECTED_RESULT ? "PASSED" : "FAILED";
    console.log(
      `${LOG_TEST_NAME}: ${LOG_TEST_RESULT}\n\tInput: ${input}\n\tExpected: ${expectedOutput}\n\tGot: ${output}\n`
    );

    return IS_EXPECTED_RESULT;
  }).length;

  console.log(`Tests ${passedTests} of ${testSamples.length} passed`);
};

runTests();
