/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */

const readline = require('readline');

const letterAValue = 'a'.charCodeAt(0);

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const getResume = (word) => [...word]
  .map((letter) => `${letter} = ${letter.charCodeAt(0) - letterAValue + 1}\n`)
  .join('');

function calculatePoints(word) {
  let points = 0;
  for (let i = 0; i < word.length; i++) {
    const letter = word[i];
    if (letter >= 'a' && letter <= 'z') {
      points += letter.charCodeAt(0) - letterAValue + 1;
    }
  }
  return points;
}

function jugar() {
  rl.question('Introduce una palabra: ', (word) => {
    const points = calculatePoints(word.toLowerCase());
    console.log(`\nPuntos de "${word}": ${points}`);
    console.log(`${getResume(word)}`);

    if (points === 100) {
      console.log('¡Felicidades! Has alcanzado 100 puntos.');
      rl.close();
    } else {
      jugar();
    }
  });
}

jugar();

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
