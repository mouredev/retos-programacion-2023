// install deps: npm install prompt-sync
const prompt = require('prompt-sync')();

function getCharPoints(char)
{
  return char.charCodeAt(0) - "A".charCodeAt(0) + 1;
}

function calculatePoints(word)
{
  let points = 0;

  for (letter of word) {
    points += getCharPoints(letter);
  }

  return points;
}

function checkWord(word)
{
  return /^[A-Z]+$/i.test(word);
}

function getWordFromUser()
{
  return prompt('Word: ').toUpperCase();
}

let win = false;

while (!win) {
  const w = getWordFromUser();

  if (!checkWord(w)) {
    console.log("Wrong word, introduce other one.");
    continue;
  }

  console.log(`Word introduced: ${w}`);

  const points = calculatePoints(w);

  console.log(`Points: ${points}`);

  if (points === 100)
    win = true;
}

console.log("You win!");
