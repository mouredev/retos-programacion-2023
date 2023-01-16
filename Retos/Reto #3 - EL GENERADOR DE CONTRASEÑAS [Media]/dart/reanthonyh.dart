import 'dart:math';

void main(List<String> args) {
  final defaultPassword = generatePassword();
  print("Default Password: $defaultPassword");

  final LargePassword = generatePassword(length: 100);
  print("Large Password: $LargePassword");

  final NoSymbolsPassword = generatePassword(length: 10, noSymbols: true);
  print("Password withOut Symbols: $NoSymbolsPassword");

  final NoMayusPassword = generatePassword(length: 10, noCaps: true);
  print("Password withOut CapsLock: $NoMayusPassword");

  final NoNumbersPassword = generatePassword(length: 12, noNumbers: true);
  print("Password withOut Numbers: $NoNumbersPassword");

  final simplePassword = generatePassword(
      noNumbers: true, noCaps: true, noSymbols: true, length: 14);
  print("Password only minus: $simplePassword");
}

String generatePassword({
  int length = 8,
  bool noCaps = false,
  bool noNumbers = false,
  bool noSymbols = false,
}) {
  String finalPassword = "";
  final lengthPassword = min(max(length, 8), 16);

  final availableChars = [
    GroupCharacters(min: 97, max: 122),
  ];

  if (!noCaps) {
    availableChars.add(GroupCharacters(min: 65, max: 90));
  }
  if (!noNumbers) {
    availableChars.add(GroupCharacters(min: 48, max: 57));
  }
  if (!noSymbols) {
    availableChars.addAll([
      GroupCharacters(min: 33, max: 47),
      GroupCharacters(min: 58, max: 96),
      GroupCharacters(min: 123, max: 125),
    ]);
  }

  for (var i = 0; i < lengthPassword; i++) {
    int random = Random().nextInt(availableChars.length);
    finalPassword += availableChars[random].getCharacter();
  }

  return finalPassword;
}

class GroupCharacters {
  const GroupCharacters({required this.min, required this.max});

  final int min;
  final int max;

  int get _length => max - min;
  String getCharacter() {
    final int random = Random().nextInt(this._length) + min;
    return String.fromCharCode(random);
  }
}
