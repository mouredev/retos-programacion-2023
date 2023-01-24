import 'dart:convert';
import 'dart:math';

void main(List<String> args) {
  PasswordGenerator passG =
      PasswordGenerator(length: 15, capitalLetter: true, number: true);
  print(passG.generate());
}

class PasswordGenerator {
  int _length;
  bool _capitalLetter;
  bool _number;
  bool _symbol;
  AsciiCodec _asciiCodec = AsciiCodec();

  PasswordGenerator(
      {int length = 8,
      bool capitalLetter = false,
      bool number = false,
      bool symbol = false})
      : _length = length < 8
            ? 8
            : length > 16
                ? 16
                : length,
        _capitalLetter = capitalLetter,
        _number = number,
        _symbol = symbol;

  String generateNumber(int value) =>
      _asciiCodec.decode([48 + value % 10]); // 0123456789

  String generateUpperLetter(int value) =>
      _asciiCodec.decode([65 + value % 26]); // ABCDEFGHIJKLMNOPQRSTUVWXYZ

  String generateLetter(int value) =>
      _asciiCodec.decode([97 + value % 26]); // abcdefghijklmnopqrstuvwxyz

  String generateSymbol(int value) {
    List<List<int>> ranges = <List<int>>[
      [33, 15], // !"#$%&'()*+,-./
      [58, 7], // :;<=>?@
      [91, 6], // [\]^_`
      [123, 4], // `{|}~
    ];
    int range = Random().nextInt(ranges.length);
    return _asciiCodec.decode([ranges[range][0] + value % ranges[range][1]]);
  }

  String generate() {
    Random random = Random();
    String output = '';
    bool hasLetter = false;
    bool hasCapital = !_capitalLetter;
    bool hasNumber = !_number;
    bool hasSymbol = !_symbol;

    while (!hasLetter || !hasCapital || !hasNumber || !hasSymbol) {
      hasLetter = false;
      hasCapital = !_capitalLetter;
      hasNumber = !_number;
      hasSymbol = !_symbol;
      output = '';
      for (var i = 0; i < _length; i++) {
        if (_capitalLetter && random.nextBool()) {
          hasCapital = true;
          output += generateUpperLetter(random.nextInt(1000000));
        } else if (_number && random.nextBool()) {
          hasNumber = true;
          output += generateNumber(random.nextInt(1000000));
        } else if (_symbol && random.nextBool()) {
          hasSymbol = true;
          output += generateSymbol(random.nextInt(1000000));
        } else {
          hasLetter = true;
          output += generateLetter(random.nextInt(1000000));
        }
        ;
      }
    }

    return output;
  }

  @override
  String toString() =>
      'PasswordGenarator: length->$_length capitals->$_capitalLetter numbers->$_number symbols->$_symbol';
}
