import 'dart:io';

void main(List<String> arguments) {
  generateMultiplicationTable();
}

int getNumber() {
  print('Ingrese un número:');
  return int.parse(stdin.readLineSync()!);
}

void generateMultiplicationTable() {
  final int value = getNumber();

  for (var i = 1; i <= 10; i++) {
    print('$value x $i = ${value * i}');
  }
}
