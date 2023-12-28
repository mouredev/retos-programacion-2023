import 'dart:math';

void main() {
  generatePassword(length: 6);
  generatePassword();
  generatePassword(length: 16, capitals: true);
  generatePassword(length: 16, capitals: true, numbers: true);
  generatePassword(length: 16, capitals: true, numbers: true, symbols: true);
}

generatePassword({int length = 8, bool capitals = false, bool numbers = false, bool symbols = false}) {
  if (length >= 8 && length <= 16) {
    var _letters = [for (var i = 97; i <= 122; i++) i];
    var _capitals = [for (var i = 65; i <= 90; i++) i];
    var _numbers = [for (var i = 48; i <= 57; i++) i];
    var _symbols = [for (var i = 33; i <= 47; i++) i] + [for (var i = 58; i <= 96; i++) i] + [for (var i = 123; i <= 125; i++) i];

    var _availableChar = [_letters];

    if (capitals) {
      _availableChar.add(_capitals);
    }
    if (numbers) {
      _availableChar.add(_numbers);
    }
    if (symbols) {
      _availableChar.add(_symbols);
    }

    Random _random = Random();

    final password = List.generate(length, (index) {
      var i = _random.nextInt(_availableChar.length);
      return String.fromCharCode(_availableChar[i][_random.nextInt(_availableChar[i].length)]);
    }).join();
    print('Generated Password: $password');
  } else {
    print('Error: Length must be between 8 and 16');
  }
}
