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

import 'dart:io';

void main() {
  hatSelection();
}

void hatSelection() {
  List<Map> questions = [
    {
      'question':
          'Si deseas quitarle la varita a tu oponente, ¿con que hechizo lo harias?',
      'answers': [
        'Accio: Atrae un objeto a las manos del lanzador',
        'Atabraquium: Ata firmemente las manos del objetivo',
        'Expelliarmus: Desarma a tu objetivo sin herirlo',
        'Crucio: Genera un dolor insoportable y torturador a la víctima'
      ]
    },
    {
      'question':
          'Si encuentras un mago mendigando en las puertas de Hogwarts, ¿que harias?',
      'answers': [
        'Le invito a mi casa y le doy cobijo mientras se recupera',
        'Le doy un poco de dinero para que pueda comer',
        'Le ayudo a encontrar un trabajo y volver a tener una buena vida',
        'Le escupo y le digo que es escoria'
      ]
    }
  ];

  int gryffindor = 0;
  int hufflepuff = 0;
  int ravenclaw = 0;
  int slytherin = 0;

  for (var i = 0; i < questions.length; i++) {
    stdout.write(questions[i]['question'] + '\n');
    for (var idx = 0; idx < questions[i]['answers'].length; i++) {
      stdout.write('${idx + 1} - ' + questions[i]['answers'][idx] + '\n');
    }
    stdout.write('Enter the number of your answer: \n');
    var answer = stdin.readLineSync();
    switch (answer) {
      case '1':
        gryffindor++;
        break;
      case '2':
        hufflepuff++;
        break;
      case '3':
        ravenclaw++;
        break;
      case '4':
        slytherin++;
        break;
      default:
        print('Invalid answer');
    }
  }

  String result = '';
  List points = [gryffindor, hufflepuff, ravenclaw, slytherin];

  points.reduce((value, element) {
    value < element ? result = 'Gryffindor' : null;
    return value;
  });

  print('Tu casa será: $result');
}
