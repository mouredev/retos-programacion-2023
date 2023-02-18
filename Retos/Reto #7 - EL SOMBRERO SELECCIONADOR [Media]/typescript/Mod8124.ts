// Crea un programa que simule el comportamiento del sombrero selccionador del
// universo mágico de Harry Potter.
// - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
// - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
// - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
//  coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
// - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
//   Por ejemplo, en Slytherin se premia la ambición y la astucia.*/

// Gryffindor: Conocidos por su valentía, coraje, caballerosidad y determinación. Los colores de la casa son escarlata y oro, y la mascota es un león.
// Slytherin: Conocidos por su ambición, astucia, ingenio y orgullo. Los colores de la casa son verde y plata, y la mascota es una serpiente.
// Ravenclaw: Conocidos por su inteligencia, ingenio, creatividad y sabiduría. Los colores de la casa son azul y bronce, y la mascota es un águila.
// Hufflepuff: Conocidos por su lealtad, paciencia, trabajo duro y juego limpio. Los colores de la casa son amarillo y negro, y la mascota es un tejón.

const { createInterface } = require('readline');

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

interface Ipoints {
  [key: string]: number;
};

interface IhousesMap {
  [key: string]: string;
};

const questions: string[] = [
  '¿Cuál de las siguientes opciones odiaría más que la gente te llamara?',
  'De estos animales ¿cual te gusta más?',
  'Dada la opción, preferirías inventar una poción que garantizara:',
  '¿Cómo le gustaría ser conocido en la historia?',
  'De estos colores ¿cuales te llaman mas la atencion?',
  'Si pudieras tener algún poder, ¿cuál elegirías?',
];

const options: string[][] = [
  ['A) Cobarde', 'B) Ordinario', 'C) Ignorante', 'D) Egoista'],
  ['A) leon', 'B) serpiente', 'C) águila', 'D) tejón'],
  ['A) Gloria', 'B) Poder', 'C) Sabiduria ', 'D) Amor'],
  ['A) El audaz', 'B) El gran', 'C) El sabio', 'D) El bueno'],
  [
    'A) Escarlata y Dorado',
    'B) Verde y Plateado',
    'C) Azul y bronce',
    'D) Amarrilo y Negro',
  ],
  [
    'A) El poder de la invisibilidad',
    'B) El poder de cambiar el pasado',
    'C) El poder de leer la mente',
    'D) El poder de cambiar tu apariencia a voluntad',
  ],
];

const houses = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'];

const points: Ipoints = {
  a: 0, //gryffindor
  b: 0, //slytherin
  c: 0, //hufflepuff
  d: 0, //ravenclaw
};

const belongTo = (points: Ipoints) => {
  let highestValue = 0;
  let highestKey = '';

  for (let key in points) {
    if (points[key] > highestValue) {
      highestValue = points[key];
      highestKey = key;
    }
  }

  const houseMap: IhousesMap = {
    a: houses[0],
    b: houses[1],
    c: houses[2],
    d: houses[3],
  };

  console.log('Tu casa de Harry Potter es ' + houseMap[highestKey]);
};

const answerQuestion = (questions: string[], options: string[][]) => {
  if ((questions.length === 0, options.length === 0)) {
    belongTo(points);
    rl.close();
    return;
  }

  const questionsLeft = questions.slice(1);
  const optionsLeft = options.slice(1);
  const index = 0;

  console.log('Solo respuesta con a,b,c,d');
  rl.question(
    questions[index] +
      options[index].map((option) => '\n' + option).join('') +
      '\n',
    (answer: string) => {
      points[answer] += 1;
      answerQuestion(questionsLeft, optionsLeft);
    }
  );
};

answerQuestion(questions, options);
