import 'dart:io';

void main() {
  final List<int> konamiCode = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];
  int konamiCodeIndex = 0;

  stdin.echoMode = false;
  stdin.lineMode = false;

  stdin.listen((keyCode) {
    if (keyCode[0] == konamiCode[konamiCodeIndex]) {
      konamiCodeIndex++;
      if (konamiCodeIndex == konamiCode.length) {
        print('Código Konami detectado');
        exit(0);
      }
    } else {
      konamiCodeIndex = 0;
    }
  });
}
