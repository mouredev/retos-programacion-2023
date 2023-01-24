import 'dart:io';

void main(List<String> args) {
  String? option = 'S';
  while (option!.toUpperCase() == 'S') {
    stdout.write("Ingrese un número: ");
    String? input = stdin.readLineSync();

    int? inputInt = int.tryParse(input ?? '');
    if (inputInt != null && inputInt > 0) {
      bool isPrime = NumberClassifier.isPrime(inputInt);
      bool isFibonacci = NumberClassifier.isFibonacci(inputInt);
      bool isPair = NumberClassifier.isPair(inputInt);

      stdout.writeln('$inputInt ${isPrime ? 'es' : 'no es'} primo,' +
          ' ${isFibonacci ? 'es' : 'no es'} fibonacci' +
          ' y es ${isPair ? 'par' : 'impar'}. ');
    } else {
      stdout.writeln('No ingreso un número válido');
    }
    stdout.write("Desea continuar[S/N]: ");
    option = stdin.readLineSync() ?? 'N';
  }
  stdout.writeln("Programa finalizado.");
}

abstract class NumberClassifier {
  static bool isPair(int number) => number & 1 == 0;

  static bool isFibonacci(int number) {
    int previous = 1;
    int current = 1;
    while (current < number) {
      int tmp = current;
      current += previous;
      previous = tmp;
    }
    return current == number;
  }

  static bool isPrime(int number) {
    int current = number ~/ 2;
    while (current > 1 && number % current != 0) {
      current--;
    }
    return number > 1 && current <= 1;
  }
}
