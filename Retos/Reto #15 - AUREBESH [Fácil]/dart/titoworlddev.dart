/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */

void main() {
  print(aurebeshTranslator('¡Hola mundo!'));
  print(aurebeshTranslator('¡HerfOskLethAurek MernUskNernDornOsk!'));
}

aurebeshTranslator(String textFromTranslate) {
  const dictionary = {
    'a': 'Aurek',
    'b': 'Besh',
    'c': 'Cresh',
    'd': 'Dorn',
    'e': 'Esk',
    'f': 'Forn',
    'g': 'Grek',
    'h': 'Herf',
    'i': 'Isk',
    'j': 'Jenth',
    'k': 'Krill',
    'l': 'Leth',
    'm': 'Mern',
    'n': 'Nern',
    'ñ': 'Ñem',
    'o': 'Osk',
    'p': 'Peth',
    'q': 'Qek',
    'r': 'Resh',
    's': 'Senth',
    't': 'Trill',
    'u': 'Usk',
    'v': 'Vev',
    'w': 'Wesk',
    'x': 'Xesh',
    'y': 'Yirt',
    'z': 'Zerek',
  };
  bool isAurebesh =
      dictionary.values.any((value) => textFromTranslate.contains(value));

  String textTranslated = '';
  if (isAurebesh) {
    textTranslated = textFromTranslate;
    for (String value in dictionary.values) {
      textTranslated = textTranslated.replaceAll(value,
          dictionary.entries.singleWhere((elem) => elem.value == value).key);
    }
  } else {
    for (String char in textFromTranslate.split('')) {
      textTranslated += dictionary[char.toLowerCase()] ?? char;
    }
  }

  return textTranslated.replaceFirstMapped(
      RegExp(r'\w'), (m) => m[0]!.toUpperCase());
}
