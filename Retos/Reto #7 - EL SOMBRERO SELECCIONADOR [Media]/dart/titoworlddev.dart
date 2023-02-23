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
import 'dart:math' as math;

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
          'Si pudieras tener cualquier superpoder, ¿cuál sería y por qué?',
      'answers': [
        'Poder volar, para sentir la libertad de los cielos.',
        'Poder curar, para ayudar a las personas necesitadas.',
        'Poder teletransportarse, para poder viajar a cualquier lugar en un instante.',
        'Poder leer la mente, para tener una ventaja en cualquier situación.'
      ]
    },
    {
      'question':
          '¿Cómo te describirías a ti mismo/a en una situación de conflicto?',
      'answers': [
        'Siempre defenderé lo que es correcto, incluso si es difícil.',
        'Trataré de encontrar una solución que sea justa para todos.',
        'Analizaré la situación con cuidado y trataré de encontrar una solución lógica.',
        'Haré lo que sea necesario para ganar y salir victorioso.'
      ]
    },
    {
      'question': '¿Qué te parece más importante: la verdad o la compasión?',
      'answers': [
        'La verdad siempre debe ser lo más importante.',
        'La compasión y la empatía son más importantes que la verdad.',
        'La verdad y la compasión deben ser igualmente importantes en cualquier situación.',
        'Depende de la situación, pero en general la verdad es más importante.'
      ]
    },
    {
      'question':
          '¿Qué cualidad crees que es más importante en un mago o bruja?',
      'answers': [
        'Coraje y valentía.',
        'Lealtad y amistad.',
        'Inteligencia y curiosidad.',
        'Ambición y determinación.'
      ]
    },
    {
      'question': '¿Qué opinas sobre el trabajo en equipo?',
      'answers': [
        'El trabajo en equipo es esencial para alcanzar objetivos importantes.',
        'El trabajo en equipo es importante, pero también es importante mantener la independencia y la individualidad.',
        'El trabajo en equipo puede ser beneficioso si todos los miembros están motivados y comprometidos.',
        'El trabajo en equipo puede ser útil para alcanzar objetivos específicos, pero también puede ser una debilidad si no se confía en los demás.'
      ]
    },
    {
      'question': '¿Cuál es tu opinión sobre el poder?',
      'answers': [
        'El poder debe ser utilizado para proteger y ayudar a los demás.',
        'El poder es peligroso y debe ser utilizado con precaución.',
        'El poder es una herramienta importante que puede ser utilizada para hacer el bien.',
        'El poder es necesario para lograr objetivos importantes.'
      ]
    },
    {
      'question': '¿Cómo te sientes acerca de las reglas y regulaciones?',
      'answers': [
        'Las reglas son importantes y deben seguirse estrictamente.',
        'Las reglas son importantes, pero deben ser flexibles para adaptarse a diferentes situaciones.',
        'Las reglas son necesarias para mantener la orden, pero también deben ser cuestionadas y revisadas regularmente.',
        'Las reglas son a menudo innecesarias y limitan la libertad.'
      ]
    },
    {
      'question': '¿Cómo actúas ante una situación conflictiva?',
      'answers': [
        'Actúo impulsivamente para proteger lo que es justo.',
        'Busco una solución pacífica y trato de encontrar un acuerdo.',
        'Analizo la situación para encontrar la mejor solución basada en la razón y el conocimiento.',
        'Busco obtener una ventaja para mi propio beneficio.'
      ]
    },
    {
      'question':
          '¿Qué crees que es más importante: la fuerza física o la fuerza mental?',
      'answers': [
        'La fuerza física es más importante.',
        'Ambas son importantes y complementarias.',
        'La fuerza mental es más importante.',
        'No creo que ninguna de las dos sea más importante que la otra.'
      ]
    },
  ];

  Map<String, int> points = {
    'Gryffindor': 0,
    'Hufflepuff': 0,
    'Ravenclaw': 0,
    'Slytherin': 0,
  };
  String result = 'Gryffindor';

  stdout.write('Bienvenido a la escuela de magia y hechiceria de Hogwarts\n');
  stdout.write(
      'Es la hora de que el sombrero seleccionador nos diga la casa a la que perteneceras\n');
  stdout.write(
      'Para ello se te haran 5 preguntas y en base a tus respuestas, seras puesto en una casa\n');
  stdout.write('Recuerda contestar con total sinceridad\n\n');
  stdout.write('Presiona la tecla enter para empezar ');
  stdin.readLineSync(retainNewlines: false);
  stdout.write('\x1B[2J\x1B[0;0H');

  for (var i = 1; i <= 5; i++) {
    int rndNumber = math.Random().nextInt(questions.length);

    stdout.write('Pregunta $i: ${questions[rndNumber]['question']}\n');

    for (var idx = 0; idx < questions[rndNumber]['answers'].length; idx++) {
      stdout.write('${idx + 1} - ${questions[rndNumber]['answers'][idx]}\n');
    }
    stdout.write('\nResponde solo con el numero de la respuesta: ');

    var answer = stdin.readLineSync();
    stdout.write('\n');
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
        stdout.write(
            'Respuesta incorrecta, solo se acepta el numero de la respuesta\n');
    }
  }

  int count = 1;
  points.values.reduce((prev, curr) {
    final key = points.keys.elementAt(count);
    curr > prev ? result = key : result;
    count++;
    return math.max(prev, curr);
  });

  print('Tu casa será: $result');
}
