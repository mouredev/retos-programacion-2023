/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

/**
 * 
 * @param {*} question  - Pregunta a realizar
 * @param {*} options  - Array de opciones
 * @returns - Promise que se resuelve con la opción seleccionada
 */
function askQuestion(question, options) {
  return new Promise((resolve, reject) => {
    const formattedOptions = options.map((option, index) => `${index + 1}. ${option}`);
    rl.question(`${question}\n${formattedOptions.join('\n')}\n`, (answer) => {
      const selectedOption = parseInt(answer);
      if (isNaN(selectedOption) || selectedOption < 1 || selectedOption > options.length) {
        console.log('Respuesta no válida. Por favor, elige una opción válida.');
        reject();
      } else {
        resolve(selectedOption);
      }
    });
  });
}


async function startSortingHat() {
  console.log('¡Bienvenido al Sombrero Seleccionador de Hogwarts!');
  
  const answers = [];
  
  // Preguntas
  answers.push(await askQuestion('¿Qué cualidad valoras más?', ['Valentía', 'Ambición', 'Lealtad', 'Intelecto']));
  answers.push(await askQuestion('¿Cómo te enfrentas a los desafíos?', ['Con coraje', 'Con astucia', 'Con paciencia', 'Con sabiduría']));
  answers.push(await askQuestion('¿Cuál es tu animal favorito?', ['León', 'Serpiente', 'Tejón', 'Águila']));
  answers.push(await askQuestion('¿Qué color te gusta más?', ['Rojo', 'Verde', 'Amarillo', 'Azul']));
  answers.push(await askQuestion('¿Qué actividad disfrutas más?', ['Deportes', 'Planificación estratégica', 'Cuidar de otros', 'Estudio']));
  
  // Algoritmo de selección de casa
  const totalGryffindor = answers[0] + answers[1];
  const totalSlytherin = answers[1] + answers[3];
  const totalHufflepuff = answers[2] + answers[4];
  const totalRavenclaw = answers[4] + answers[3];
  
  const maxTotal = Math.max(totalGryffindor, totalSlytherin, totalHufflepuff, totalRavenclaw);
  
  if (maxTotal === totalGryffindor) {
    console.log('¡Eres de Gryffindor!');
  } else if (maxTotal === totalSlytherin) {
    console.log('¡Eres de Slytherin!');
  } else if (maxTotal === totalHufflepuff) {
    console.log('¡Eres de Hufflepuff!');
  } else {
    console.log('¡Eres de Ravenclaw!');
  }

  rl.close();
}

startSortingHat();
