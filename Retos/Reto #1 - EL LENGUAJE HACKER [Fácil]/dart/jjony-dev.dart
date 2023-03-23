void main() {
  final Map<String, String> code = <String, String>{
    'A': '4',
    'B': 'l3',
    'C': '[',
    'D': ')',
    'E': '3',
    'F': '|=',
    'G': '&',
    'H': '#',
    'I': '1',
    'J': ',_|',
    'K': '>|',
    'L': '1',
    'M': '/\\/\\',
    'N': '^/',
    'O': '0',
    'P': '|*',
    'Q': '(_,)',
    'R': 'l2',
    'S': '5',
    'T': '7',
    'U': '(_)',
    'V': '\\/',
    'W': '\\/\\/',
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
    ' ': ' '
  };
  String input = 'Hola mundo!, resolviendo el reto 1 del 2023.';

  print('Texto sin codificar: $input');
  Leet leet = Leet(code);
  String textEncoded = leet.encode(text: input);
  print('Texto codificado: $textEncoded');
}

class Leet {
  Map<String, String> _code;
  Leet(this._code);

  setCode(Map<String, String> newCode) {
    _code = newCode;
  }

  Map<String, String> get code => _code;

  setUnitCode({required String input, required String output}) {
    if (_code.containsKey(input)) _code[input] = output;
  }

  String encode({required String text}) {
    String encoded = '';
    for (var i = 0; i < text.length; i++) {
      String char = text[i].toUpperCase();
      _code.containsKey(char)
          ? encoded += _code[char]!
          : print(' - El caracter "$char" no puede ser codificado');
    }
    return encoded;
  }
}
