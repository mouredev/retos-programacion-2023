/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras. ok
 * - Longitud media de las palabras. ok
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

void main() {
  analizeText('Hola, me llamo Tito. Me gusta programar en Dart.');
}

void analizeText(String textToAnalize) {
  print('Texto origen: $textToAnalize');
  List textWords = textToAnalize
      .split(' ')
      .map((e) => e.replaceAll(RegExp(r'\W'), ''))
      .toList();
  print('Numero total: ${textWords.length}');
  List wordsLength = textWords.map((e) => e.length).toList();
  num wordsLengthAverage =
      wordsLength.reduce((value, element) => value + element) /
          wordsLength.length;
  print('Longitud media: $wordsLengthAverage');
  List orations = textToAnalize.replaceAll(RegExp(r'[^.]'), '').split('');
  print('Número de oraciones: ${orations.length}');
  wordsLength.sort((a, b) => b - a);
  print('Palabra más larga: ${wordsLength[0]}');
}
