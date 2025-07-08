import { createInterface } from "node:readline/promises";

const words = ["javascript", "programacion", "desarrollo", "platano"];

// palabra completa
const randomWord = words[Math.floor(Math.random() * words.length)];

let attempts = 6;

const hiddenLetters = Math.floor(randomWord.length * 0.6);

const hiddenLettersPosition = getRandomNumbers(
  0,
  randomWord.length - 1,
  hiddenLetters
);

// palabra escondida
let hiddenWord = "";

for (let i = 0; i < randomWord.length; i++) {
  const letter = randomWord[i];
  hiddenWord += hiddenLettersPosition.has(i) ? "_" : letter;
}

function getRandomNumbers(min, max, times) {
  const letters = new Set();

  while (letters.size < times) {
    const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;
    letters.add(randomNumber);
  }

  return letters;
}

async function main() {
  while (attempts > 0 && hiddenWord.includes("_")) {
    console.log(`ADIVINA LA PALABRA: ${hiddenWord}\n`);
    console.log(`Tienes ${attempts} intentos restantes.\n`);

    const text = await getInput();

    if (text.length === 1) {
      let found = false;
      for (let i = 0; i < randomWord.length; i++) {
        const letter = randomWord[i];
        if (letter === text) {
          hiddenWord =
            hiddenWord.substring(0, i) + letter + hiddenWord.substring(i + 1);
          found = true;
        }
      }

      if (found) {
        console.log(`¡Bien hecho! Has encontrado una letra.\n`);
        continue;
      }

      console.log(`La letra "${text}" no está en la palabra.\n`);
      attempts--;
    }

    if (text === randomWord) {
      break;
    } else {
      console.log("La palabra no es correcta, intenta de nuevo.\n");
      attempts--;
    }
  }

  if (attempts === 0) {
    console.log(`Lo siento, has perdido. La palabra era: ${randomWord}`);
  } else {
    console.log(
      `¡Felicidades! Has adivinado la palabra correctamente con ${
        6 - attempts
      } ${6 - attempts === 1 ? "intento" : "intentos"} perdidos.\n`
    );
  }
}


async function getInput() {
  const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const answer = await rl.question(
    "Introduce una letra o la solución completa: \n"
  );

  rl.close();

  return answer;
}


main();