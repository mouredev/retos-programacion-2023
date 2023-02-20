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
import 'dart:math';

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

  Map<String, int> points = {
    'Gryffindor': 0,
    'Hufflepuff': 0,
    'Ravenclaw': 0,
    'Slytherin': 0,
  };
  String result = 'Gryffindor';

  for (var i = 0; i < questions.length; i++) {
    stdout.write(questions[i]['question'] + '\n');

    for (var idx = 0; idx < questions[i]['answers'].length; idx++) {
      stdout.write('${idx + 1} - ' + questions[i]['answers'][idx] + '\n');
    }
    stdout.write('\nResponde solo con el numero de la respuesta: ');

    var answer = stdin.readLineSync();
    print('\n');
    switch (answer) {
      case '1':
        points['Gryffindor'] = points['Gryffindor']! + 1;
        break;
      case '2':
        points['Hufflepuff'] = points['Hufflepuff']! + 1;
        break;
      case '3':
        points['Ravenclaw'] = points['Ravenclaw']! + 1;
        break;
      case '4':
        points['Slytherin'] = points['Slytherin']! + 1;
        break;
      default:
        print('Invalid answer');
    }
  }

  int count = 1;
  points.values.reduce((prev, curr) {
    final key = points.keys.elementAt(count);
    curr > prev ? result = key : result;
    count++;
    return max(prev, curr);
  });

  print('Tu casa será: $result');
}
