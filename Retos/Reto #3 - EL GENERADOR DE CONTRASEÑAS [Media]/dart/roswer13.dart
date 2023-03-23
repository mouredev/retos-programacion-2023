import 'dart:math';

void main() {
  testCase(length: 6);
  testCase(length: 7);
  testCase(length: 8);
  testCase(length: 5);
  testCase(length: 9);
}

void testCase({length = int}) {
  var password = generatePassword(length: length);

  if (password.length != length) {
    print(
        "Case with the length: '$length', returns ${password.length} but it should be $length");
    return;
  }

  print("Password: '$password', the length '${password.length}'");
}

String generatePassword({length = int}) {
  if (length >= 6 && length <= 8) {
    final letterLowerCase = "abcdefghijklmnopqrstuvwxyz";
    final letterUpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    final number = '0123456789';
    final special = '@#%^*>\$@?/[]=+';

    String chars = "";
    chars += '$letterLowerCase$letterUpperCase';
    chars += '$number';
    chars += '$special';

    return List.generate(length, (index) {
      final indexRandom = Random.secure().nextInt(chars.length);
      return chars[indexRandom];
    }).join('');
  }

  return '';
}
