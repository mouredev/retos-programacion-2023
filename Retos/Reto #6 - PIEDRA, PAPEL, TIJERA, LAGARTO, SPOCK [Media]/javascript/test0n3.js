const contenders = {
  "✀": { win: ["📄", "🦎"], lose: ["🖖", "🗿"] },
  "📄": { win: ["🗿", "🖖"], lose: ["✀", "🦎"] },
  "🗿": { win: ["🦎", "✀"], lose: ["📄", "🖖"] },
  "🦎": { win: ["🖖", "📄"], lose: ["🗿", "✀"] },
  "🖖": { win: ["✀", "🗿"], lose: ["🦎", "📄"] },
};

const game = (arr) => {
  let resp = [0, 0];
  arr.forEach((play) => {
    if (contenders[play[0]]["win"].includes(play[1])) resp[0] += 1;
    if (contenders[play[0]]["lose"].includes(play[1])) resp[1] += 1;
  });
  return resp;
};

const rockPaperScissorsLizardSpock = (input) => {
  const resp = game(input);
  if (resp[0] == resp[1]) return "Tie";

  if (resp[0] > resp[1]) return "Player1";
  else return "Player2";
};

const tests = {
  input: [
    [
      ["🗿", "✀"],
      ["✀", "🗿"],
      ["📄", "✀"],
    ],
    [
      ["🖖", "🗿"],
      ["🗿", "🦎"],
      ["🦎", "✀"],
    ],
    [
      ["📄", "📄"],
      ["🗿", "🗿"],
      ["🖖", "🖖"],
    ],
    [
      ["🗿", "✀"],
      ["🦎", "✀"],
      ["🖖", "🖖"],
    ],
  ],
  output: ["Player2", "Player1", "Tie", "Tie"],
};
let errors = 0;
tests.input.forEach((test, index) => {
  resp = rockPaperScissorsLizardSpock(test);
  expected = tests.output[index];
  if (resp == expected) return;

  errors += 1;
  console.log(`\n\noriginal: ${test}`);
  console.log(resp);
  console.log(`expected: ${expected}`);
});

console.log(`\nTests${errors != 0 ? " not " : " "}passed, ${errors} errors\n`);
