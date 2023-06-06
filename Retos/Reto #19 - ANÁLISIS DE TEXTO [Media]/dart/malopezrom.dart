/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

import 'package:http/http.dart' as http;
import 'package:html/parser.dart' as parser;

void main(){
  
  String text = """    la luna asoma: federico garcía lorca
                       cuando sale la luna
                       se pierden las campanas
                       y aparecen las sendas
                       impenetrables.
                       cuando sale la luna,
                       el mar cubre la tierra
                       y el corazón se siente
                       isla en el infinito.
                       nadie come naranjas
                       bajo la luna llena.
                       es preciso comer
                       fruta verde y helada.
                       cuando sale la luna
                       de cien rostros iguales,
                       la moneda de plata
                       solloza en el bolsillo.
                    """.trim();

  analyzeText(text);


}

/**
 * Función que analiza un texto y obtiene:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Palabra más larga.
 */
void analyzeText(String text) {
  RegExp wordsRegex = RegExp(r'\b\w+\b');
  RegExp sentenceRegex = RegExp(r'\b\w+\.');
  List<String> words = text.replaceAll("\n"," ").split(" ");
  int sentences = 0;
  String longestWord = '';
  int length = 0;
  int size = 0;


  words.forEach((word) {

    if (wordsRegex.hasMatch(word)) {
      size++;
      if (sentenceRegex.hasMatch(word)) {
        sentences++;
      }
    }
    length += word.length;
    if (word.length > longestWord.length) {
      longestWord = word;
    }
  });

  int averageLength = length ~/ size;
  print('Total de palabras: $size');
  print('Longitud media: $averageLength');
  print('Numero de frases: $sentences');
  print('Palabra mas larga: $longestWord(${longestWord.length})');
}