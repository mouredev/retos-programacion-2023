/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

void main() {
  List testWords = [
    'hola',
    'titoworlddev',
    'moure',
    'bebe',
    'jidyanqflcezsogvbrpwtkxhmu'
  ];
  testWords.forEach((word) {
    print('Word: $word');
    print('Heterogram: ${isHeterogram(word)}');
    print('Isogram: ${isIsogram(word)}');
    print('Pangram: ${isPangram(word)}');
    print('');
  });
}

bool isHeterogram(String text) {
  // palabra o frase que no tiene letras repetidas.
  List textInList = text.split('');
  Set letters = {...textInList};

  return textInList.length == letters.length;
}

bool isIsogram(String text) {
  // palabra o frase en la que cada letra aparece el mismo número de veces
  List textInList = text.split('');
  Set letters = {...textInList};
  Map lettersCount = {};
  letters.forEach((letter) {
    lettersCount.addEntries({'$letter': 0}.entries);
  });
  textInList.forEach((letter) => lettersCount[letter]++);
  int index = -1;
  return lettersCount.values.skip(1).every((value) {
    index++;
    return value == lettersCount.values.elementAt(index);
  });
}

bool isPangram(String text) {
  // palabra o frase que contiene todas las letras del abecedario.
  String alphabet = 'abcdefghijklmnopqrstuvwxyz';
  List textInList = text.split('');
  textInList.sort();
  return {...textInList}.join() == alphabet;
}
