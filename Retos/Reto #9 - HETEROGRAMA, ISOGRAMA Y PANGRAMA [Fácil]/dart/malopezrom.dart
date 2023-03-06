/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

/**
 * Función principal
 */

main() {
  checkWord('Ecuador, cada quince de noviembre');
  checkWord('esdrújula');
  checkWord('aliento');
  checkWord('mama');
  checkWord("El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja");
  checkWord("Jovencillo emponzoñado de whisky, ¡qué figurota exhibe!");
}

/**
 * Funcione que comprueba si una palabra es un isograma, pangrama o heterograma
 */
void checkWord(String word){


  String message = 'La frase ${word} es : ';
  List<String> conditions = [];

  if (isIsogram(word)) {
    conditions.add('isograma');
  }

  if (isPangram(word)) {
    conditions.add('pangrama');
  }

  if (isHetereogram(word)) {
    conditions.add('heterograma');
  }

  if (conditions.isEmpty) {
    message += 'ni un isograma, ni un pangrama, ni un heterograma';
  } else {
    message += conditions.join(', ') + '.';
  }

  print(message);
}

/**
 * Funcion que detecta si una palabra es un heterograma con una expresion regular
 * Un Heterograma es una palabra que no tiene letras repetidas
 */

bool isHetereogram(String text) {
  String textLower = text.toLowerCase().cleanText().replaceAll(RegExp('[^a-z]'), '');
  RegExp regExp = new RegExp(r'^(?!.*(.).*\1)[a-zA-Z]+$');
  return regExp.hasMatch(textLower);
}

/**
 * Funcion que detecta si una palabra es un isograma.
 * Un isograma es una palabra en la que cada letra se repite exactamente el mismo numero de veces
 * Una palabra en la que cada letra se repite una sola vez es a su vez un heterograma.
 * Un palabra en la que cada letra se repite dos veces es un isograma de grado 2 y asi sucesivamente.
 */
bool isIsogram(String text) {

  Map<String, int> countLetters = {};
  String textLower = text.toLowerCase().cleanText().replaceAll(RegExp('[^a-z]'), '');
  textLower.runes.forEach((element) {
    String letter = String.fromCharCode(element);
    countLetters[letter] = RegExp(letter)
        .allMatches(textLower)
        .length;
    });

  return countLetters.values.toSet().length==1;

}

/**
 * Funcion que detecta si una palabra es un pangrama
 * Un Pangrama es una frase que contiene todas las letras del alfabeto
 */

bool isPangram(String text) {
  String textLower = text.toLowerCase().cleanText().replaceAll(RegExp('[^a-z]'), '');
  RegExp regExp = new RegExp(r'[a-z]');
  int numberOfLetters = regExp.allMatches('abcdefghijklmnopqrstuvwxyz').length;
  Set letters = regExp.allMatches(textLower).map((match) => match.group(0)).toSet();
  return letters.length == numberOfLetters;
}


/**
 * Funcion de extension de un string que limpia los acentos de una cadena de texto y
 * los sustituye por su equivalente sin acento
 */
extension StringExtension  on String {
  String cleanText() {
    final regExp = RegExp('[áéíóúÁÉÍÓÚ]');
    final accents = {
      'á': 'a',
      'é': 'e',
      'í': 'i',
      'ó': 'o',
      'ú': 'u',
      'Á': 'A',
      'É': 'E',
      'Í': 'I',
      'Ó': 'O',
      'Ú': 'U'
    };

    return this.replaceAllMapped(
        regExp, (match) => accents[match[0]!]!);
  }
}
