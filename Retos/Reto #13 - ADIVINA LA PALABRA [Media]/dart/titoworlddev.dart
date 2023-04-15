/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 * - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que la palabra a adivinar)
 * - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta uno al número de intentos
 * - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno al número de intentos
 * - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

// ignore_for_file: uri_does_not_exist
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:math' as math;
import 'dart:io';

void main() {
  hangmanGame();
}

getWord() async {
  final data = await http
      .get(Uri.parse(
          'https://random-word-api.vercel.app/api?words=1&alphabetize=true'))
      .then((res) => jsonDecode(res.body));
  String word = await data[0];
  return word;
}

// La libreria http no funciona si no estas en una app, pero se puede probar con la funcion getWord() comentada y la palabra predefinida (mouredev), eso si, hay que quitar todos los async y await
wordsTransformed() async {
  // String preWord = 'mouredev';
  String preWord = await getWord();
  String newWord = preWord;
  int wordLength = preWord.length;
  final rnd = math.Random().nextInt(3) + 3;
  // rnd / 10 es para no tener siempre el 60% de la palabra oculto
  int forLength = (wordLength * rnd / 10).round();

  for (var i = 0; i < forLength; i++) {
    final rndIndx = math.Random().nextInt(wordLength);
    if (newWord[rndIndx] != '_')
      newWord = newWord.replaceRange(rndIndx, rndIndx + 1, '_');
  }

  return {'pre': preWord, 'new': newWord};
}

hangmanGame() async {
  Map words = await wordsTransformed();
  int posibleAttempts = 10;
  int attempts = 10;
  stdout.write(
      'Este es el juego del ahorcado, y las reglas son las siguientes:\n\n');
  stdout.write(
      'Te daré una palabra en inglés con varias letras ocultas y tu tendrás que adivinar que palabra es.\n');
  stdout.write(
      'Para ello, tienes $posibleAttempts intentos, y puedes ir diciendo letras para ir descubriendo poco a poco la palabra o decir palabras directamente.\n');
  stdout.write(
      'Pero, ¡ojo! Si pones más de una letra y esta no es la palabra correcta será un fallo, \nasí que si quieres poner una letra, ten cuidado de no poner dos o más juntas.\n');
  stdout.write('Así que si esta todo claro, ¡empezemos con el juego!\n');
  stdout.write('Pulsa la tecla enter para continuar...\n');
  stdin.readLineSync();
  stdout.write('\x1B[2J\x1B[0;0H');

  do {
    if (attempts == 10) {
      stdout.write('La palabra es: [ ${words['new']} ]\n');
      stdout.write('Te quedan $attempts intentos\n');
      stdout.write('Introduce una letra o palabra: ');
    } else {
      stdout.write('Introduce una letra o palabra: ');
    }
    attempts--;
    String input = stdin.readLineSync()!.toLowerCase();

    stdout.write('\x1B[2J\x1B[0;0H');
    if (words['pre'] == input) {
      words['new'] = words['pre'];
    } else if (words['pre'].contains(input) && input.length == 1) {
      int idx = 0;
      words['new'] = words['new'].split('').map((char) {
        String newChar =
            char == '_' && words['pre'][idx] == input ? input : char;
        idx++;
        return newChar;
      }).join();
      stdout.write(
          '¡Correcto! Has acertado una letra. \nAsí está la palabra ahora [ ${words['new']} ]\n');
      stdout.write('Sigue jugando, te quedan $attempts intentos\n');
    } else if (attempts > 0) {
      stdout.write(
          '¡Incorrecto! Prueba otra letra o palabra.\nLa palabra sigue así [ ${words['new']} ]\n');
      stdout.write('Sigue jugando, te quedan $attempts intentos\n');
    } else {
      attempts = 0;
    }
  } while (words['new'] != words['pre'] && attempts > 0);

  if (words['new'] == words['pre']) {
    stdout.write('\x1B[2J\x1B[0;0H');
    stdout.write('\n¡Increible! Palabra completada.\n');
    stdout.write('¡Enhorabuena! ¡Has ganado el juego!\n');
    stdout.write('Lo has completado en ${10 - attempts} intentos.\n');
    stdout.write('¡Eres genial!');
  } else if (attempts == 0) {
    stdout.write(
        '\nLo siento, no te quedan más intentos, has perdido el juego.\n');
    stdout.write(
        'Pero no pasa nada, puedes volver a intentarlo, no te rindas.\n');
  }
}
