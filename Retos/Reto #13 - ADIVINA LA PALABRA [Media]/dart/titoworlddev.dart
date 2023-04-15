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
  final data = await http.get(Uri.parse('https://random-word-api.vercel.app/api?words=1&alphabetize=true'))
    .then((res) => jsonDecode(res.body));
  String word = await data[0];
  return word;
}

wordTransformed() async {
  String preWord = await getWord();
  String newWord = preWord;
  int wordLength = preWord.length;
  final rnd = math.Random().nextInt(3) + 3;
  // rnd / 10 es para no tener siempre el 60% de la palabra oculto
  int forLength =(wordLength * rnd / 10).round();
  
  for(var i = 0; i < forLength; i++) {
    final rndIndx = math.Random().nextInt(wordLength);
    if(newWord[rndIndx] != '_') newWord = newWord.replaceRange(rndIndx, rndIndx + 1, '_');
  }
  
  return {preWord, newWord};
}

hangmanGame() async {
  Map word = await wordTransformed();
  int attempts = 10;
  stdout.write('Este es el juego del ahorcado, y las reglas son las siguientes:');
  stdout.write('Te daré una palabra en inglés con varias letras ocultas y tu tendrás que adivinar que palabra es.')
  stdout.write('Para ello, tienes $attempts intentos, y puedes ir diciendo letras');
  stdout.write('para ir descubriendo poco a poco la palabra o palabras directamente.');
  stdout.write('Así que si esta todo claro, ¡empezemos con el juego!');
  stdout.write('Pulsa cualquier tecla para continuar');
  stdin.readLineSync();
  stdout.write('Terminado');
}



