import 'dart:io';
void main() {
  while (true) {
    stdout.write("Introduce tu numero:\r\n");
    int number = int.parse(stdin.readLineSync()!);
    print('$number ' + isPrime(number) + ', ' +
          isFibonacci(number) + ' y ' + isEven(number));
  }
}

String isPrime(int number) {
  if (number == 1) {
    return "no es primo";
  }
  for (var i = 2; i < number; i++) {
    if (number % i == 0) {
      return "no es primo";
    }
  }
  return "es primo";
}

String isFibonacci(int number) {
  var a = 0;
  var b = 1;
  while (b < number) {
    var temp = a;
    a = b;
    b = temp + b;
  }
  return b == number ? "fibonacci" : "no es fibonacci";
}

String isEven(int number) {
  return number % 2 == 0 ? "es par" : "es impar";
}