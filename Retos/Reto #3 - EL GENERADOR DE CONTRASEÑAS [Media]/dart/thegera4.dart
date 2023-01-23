import 'dart:math';

void main() {
  generateRandomPassword();
}

void generateRandomPassword() {
  var password = '';
  var random = Random.secure();
  for (var i = 0; i < random.nextInt(8) + 8; i++) {
    var charCode = random.nextInt(94) + 33;
    password += String.fromCharCode(charCode);
  }
  print('Tu nueva contraseña es: $password');
}
