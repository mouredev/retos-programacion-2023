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

void main() async {
  print(await getWord());
}

getWord() async {
  final data = await http.get(Uri.parse('https://random-word-api.vercel.app/api?words=10'))
    .then((res) => jsonDecode(res.body));
  List words = await data;
  final random = math.Random().nextInt(words.length);
  return words[random];
}

wordTransformed() async {
  final random = math.Random().nextInt(words.length);
  String preWord = await getWord();
  String newWord = preWord.
}