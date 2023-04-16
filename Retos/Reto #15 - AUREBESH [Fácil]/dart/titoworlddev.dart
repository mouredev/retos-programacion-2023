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
  print(traduceAurebesh('hola mundo'));
//   print(traduceAurebesh('HerfOskLethAurek MernUskNernDornOsk'));
}

traduceAurebesh(String textFromTranslate) {
  const dictionaryToSpanish = {
    'Aurek': 'a',
    'Besh': 'b',
    'Cresh': 'c',
    'Dorn': 'd',
    'Esk': 'e',
    'Forn': 'f',
    'Grek': 'g',
    'Herf': 'h',
    'Isk': 'i',
    'Jenth': 'j',
    'Krill': 'k',
    'Leth': 'l',
    'Mern': 'm',
    'Nern': 'n',
    'Ñem': 'ñ',
    'Osk': 'o',
    'Peth': 'p',
    'Qek': 'q',
    'Resh': 'r',
    'Senth': 's',
    'Trill': 't',
    'Usk': 'u',
    'Vev': 'v',
    'Wesk': 'w',
    'Xesh': 'x',
    'Yirt': 'y',
    'Zerek': 'z',
  };
  const dictionaryToAurebesh = {
    'a': 'Aurek',
    'ae': 'Enth',
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

  bool isAurebesh = dictionaryToAurebesh.values
          .any((value) => textFromTranslate.startsWith(value)) ||
      dictionaryToAurebesh.values
          .any((value) => textFromTranslate.endsWith(value));

  String textTranslated = textFromTranslate;
  textFromTranslate.split(' ').forEach((word) {
    if (isAurebesh) {
      for (String key in dictionaryToSpanish.keys) {
        textTranslated =
            textTranslated.replaceAll(key, dictionaryToSpanish[key]!);
      }
    } else {
      for (String key in dictionaryToAurebesh.keys) {
        textTranslated =
            textTranslated.replaceAll(key, dictionaryToAurebesh[key]!);
      }
    }
  });

  return textTranslated;
}
