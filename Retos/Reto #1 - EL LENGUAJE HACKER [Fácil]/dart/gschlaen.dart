import 'dart:io';

void main(List<String> arguments) {
  print('Ingresa el texto que quieres codificar...');
  String? text = stdin.readLineSync();
  if (text != null) {
    translateToHacker(text);
  }
}

translateToHacker(String text) {
  final Map<String, String> hackerCode = {
    'A': '4',
    'B': '8',
    'C': '(',
    'D': '|)',
    'E': '3',
    'F': '|=',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': ',_|',
    'K': '|<',
    'L': '1',
    'M': r'/\/\',
    'N': '^/',
    'O': '0',
    'P': '|*',
    'Q': '(_,)',
    'R': 'I2',
    'S': '5',
    'T': '7',
    'U': '(_)',
    'V': r'\/',
    'W': r'\/\/',
    'X': '><',
    'Y': 'j',
    'Z': '2',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'o',
  };

  final upperText = text.toUpperCase();
  String translation = '';
  for (int i = 0; i < upperText.length; i++) {
    if (hackerCode.containsKey(upperText[i])) {
      translation += hackerCode[upperText[i]]!;
    } else {
      translation += upperText[i];
    }
  }
  print('Texto original: $text');
  print('Texto codificado: $translation');
}
