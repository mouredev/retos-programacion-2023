/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

const prompt = require('prompt-sync')();

type HPQuestion = {question: string; answers: string[]};

class SelectHat {
  questions: HPQuestion[];
  posibilities: string[];

  constructor(database: HPQuestion[], posibilities: string[]) {
    this.questions = database;
    this.posibilities = posibilities;
  }

  async askQuestions() {
    const answers = [0, 0, 0, 0];
    console.log('-------Inicio------');
    for (const question of this.questions) {
      let text = question.question + '\n';
      question.answers.forEach((answer: string, index: number) => {
        text += `${index} ${answer} \n`;
      });
      let selection = -1;
      let goodAnswer = false;
      while (!goodAnswer) {
        goodAnswer = false;
        selection = -1;
        const userSelection = prompt(text);
        selection = Number.parseInt(userSelection || '-1');
        if ([0, 1, 2, 3].includes(selection)) {
          goodAnswer = true;
        }
      }
      answers[selection]++;
    }
    let max = 0;
    let maxPoints = 0;
    answers.forEach((answer: number, index: number) => {
      if (answer > maxPoints) {
        max = index;
        maxPoints = answer;
      }
    });
    console.log(`Tu casa es: ${posibilities[max]}`);
  }
}

const quest: HPQuestion[] = [
  {
    question: 'Que color te gusta mas?',
    answers: ['Rojo', 'Verde', 'Amarillo', 'Azul'],
  },
  {
    question: 'Que animal prefieres?',
    answers: ['Leon', 'Serpiente', 'Oso', 'Cuervo'],
  },
  {
    question: 'Que te representa mas?',
    answers: ['Valor', 'Ambicion', 'Justicia', 'Creatividad'],
  },
  {
    question: 'Con quien te identificas?',
    answers: ['Harry Poter', 'Draco Malfoy', 'Cedric Diggory', 'Luna Lovegood'],
  },
  {
    question: 'Que elemento te gusta mas?',
    answers: ['Fuego', 'Agua', 'Tierra', 'Aire'],
  },
];

const posibilities = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'];

const quizz = new SelectHat(quest, posibilities);

quizz.askQuestions();
