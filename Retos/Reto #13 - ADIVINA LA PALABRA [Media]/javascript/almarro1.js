/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
const readline = require('readline').createInterface({ input: process.stdin, output: process.stdout, prompt: 'guess>' });

/**
 * Function that returns a random word from a predefined set and a max length
 */
function generateRandomWord(maxLength = 8) {
  //TODO: implement
  return 'mouredev';
}

/**
 * Function that returns an obfuscated version of the word by replacing unkown letters
 * with a "_"
 * @param {*} word the word to obfuscate
 * @param {*} knownLetters an array with the letters that must not be obfuscated
 */
function obfuscateWord(word, knownLetters = []) {
  return word.split('').map((letter) => knownLetters.includes(letter) ? letter : '_').join('');
}

/**
 * Given a word, it provides enough known letters so there are no more that ```threshold```% hidden
 * @param {*} word the original word
 * @param {*} threshold max percentage of hidden letters
 */
function randomizeKnownLetters(word, threshold = 0.6) {
  let knownPerc = 1;
  const knownLetters = new Set(word.split(''));
  let deletedLetter;
  while (knownPerc > (1 - threshold)) {
    deletedLetter = [...knownLetters][Math.floor(Math.random() * knownLetters.size)];
    knownLetters.delete(deletedLetter);
    knownPerc = word.split('').filter((letter) => knownLetters.has(letter)).length / word.length;
  }
  //we add that letter back to be below the hidden letters threshold
  return [...knownLetters.add(deletedLetter)];
}

/**
 * Function that checks if a word contains a letter
 * @param {*} word
 * @param {*} letter
 */
function checkLetter(word, letter) {
  return word.split('').includes(letter);
}

async function newGame(maxAttemps = 10) {
  const word = generateRandomWord();
  const allLetters = new Set(word.split(''));
  const knownLetters = randomizeKnownLetters(word, 0.6);
  let attempsLeft = maxAttemps;
  let guessed = false; // control if the player guessed the word
  while (!guessed && attempsLeft > 0) {
    const response = await new Promise(resolve => readline.question(`Give me another guess for ${obfuscateWord(word, knownLetters)}. You have ${attempsLeft} attemps left: `, resolve));

    if (response.length === 1 && checkLetter(word, response)) {
      knownLetters.push(response);
      const knownSet = [...new Set(knownLetters)];
      guessed = knownSet.length === allLetters.size && knownSet.every((letter) => allLetters.has(letter));
    } else if (response.length === word.length && response.toLocaleLowerCase() === word) {
      guessed = true;
    } else {
      attempsLeft--;
    }

  }

  if (guessed) {
    console.log('You guessed the word!!!');
  }
  if (attempsLeft === 0) {
    console.log('You lost!!! You have no attemts left');
  }
  readline.close();
}

newGame();