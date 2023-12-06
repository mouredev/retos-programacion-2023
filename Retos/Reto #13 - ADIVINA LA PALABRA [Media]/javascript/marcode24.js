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

const readLine = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

const MAX_ATTEMPTS = 5;

const generateWord = (length) => {
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  let word = '';
  for (let i = 0; i < length; i++) {
    word += characters[Math.floor(Math.random() * characters.length)];
  }
  return word;
};

const generateRandomLength = (min = 8, max = 12) => Math
  .floor(Math.random() * (max - min + 1) + min);

const hideSomeLetters = (word) => {
  const percentToHide = Math.floor(Math.random() * 6) + 3;
  const lettersToHide = [...word].filter((_, index) => index % percentToHide === 0);
  return [...word].map((char) => (lettersToHide.includes(char) ? '_' : char)).join('');
};

const start = () => {
  const word = generateWord(generateRandomLength());
  const guessWord = hideSomeLetters(word);
  const results = [...guessWord].map((char) => ({ char, guessed: (char !== '_') }));
  let attempts = 0;

  console.log('Welcome to the game!!!');
  console.log(`try to guess the word in ${MAX_ATTEMPTS} attempts \n`);
  console.log(`Your word is: ${guessWord}\n`);

  const askQuestion = () => {
    console.log(`You have ${MAX_ATTEMPTS - attempts} attempts left`);
    readLine.question('Enter a word: ', (answer) => {
      if (answer.length !== word.length) {
        console.log('Your word must have the same length as the hidden word\n');
        return askQuestion();
      }

      results.map((result, index) => {
        if (result.char === '_' && word[index] === answer[index]) {
          result.guessed = true;
          result.char = answer[index];
        }
        return result;
      });
      attempts++;

      if (results.every((result) => result.guessed)) {
        readLine.close();
        return console.log('\nYou won :)');
      }

      if (attempts === MAX_ATTEMPTS) {
        readLine.close();
        return console.log(`\nYou lost :( \nThe word was: ${word}`);
      }

      console.log(`\ncurrent result: ${results
        .map((result) => result.char).join('')} \n`);
      return askQuestion();
    });
  };
  askQuestion();
};

start();

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
