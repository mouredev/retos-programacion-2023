import 'dart:math';

String generatePassword({
  int passwordLength = 8,
  bool hasUpperCase = false,
  bool hasNumbers = false,
  bool hasSymbols = false,
}) {
  List<String> lowerCaseList = 'abcdefghijklmnopqrstuvwxyz'.split('');
  List<String> upperCaseList = [
    ...lowerCaseList.map((letter) => letter.toUpperCase())
  ];
  List<String> numbersList = '0123456789'.split('');
  List<String> symbolsList = '.?,;-_¡!¿*%&\$/()[]{}|@><'.split('');

  List<String> charactersList = [...lowerCaseList];
  if (hasUpperCase) charactersList.addAll(upperCaseList);
  if (hasNumbers) charactersList.addAll(numbersList);
  if (hasSymbols) charactersList.addAll(symbolsList);

  String generatedPassword = '';

  for (int i = 0; i < passwordLength; i++) {
    int randomNumber = Random().nextInt(charactersList.length);
    generatedPassword += charactersList[randomNumber];
  }

  return generatedPassword;
}

void main() {
  print('Password 1: ${generatePassword()}');
  print(
      'Password 2: ${generatePassword(passwordLength: 12, hasUpperCase: true)}');
  print(
      'Password 3: ${generatePassword(passwordLength: 10, hasUpperCase: true, hasNumbers: true)}');
  print(
      'Password 4: ${generatePassword(passwordLength: 16, hasUpperCase: true, hasNumbers: true, hasSymbols: true)}');
}
