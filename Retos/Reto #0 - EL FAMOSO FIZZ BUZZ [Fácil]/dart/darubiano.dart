/*
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
 */
void fizzBuzzJunior() {
  for (var number = 1; number <= 100; number++) {
    if (number % 3 == 0 && number % 5 == 0) {
      print("fizzbuzz");
    } else if (number % 3 == 0) {
      print("fizz");
    } else if (number % 5 == 0) {
      print("buzz");
    } else {
      print(number);
    }
  }
}

final fizzBuzzSenior = () {
  for (var number = 1; number <= 100; number++) {
    String output =
        (number % 3 == 0 ? "fizz" : "") + (number % 5 == 0 ? "buzz" : "");
    print(output.isEmpty ? number : output);
  }
};

final fizzBuzzChatgpt = () {
  List.generate(100, (number) {
    number++;
    String output =
        (number % 3 == 0 ? "fizz" : "") + (number % 5 == 0 ? "buzz" : "");
    print(output.isEmpty ? number : output);
  });
};

void main() {
  //* Solucion junior
  fizzBuzzJunior();

  // * Solucion sernior
  fizzBuzzSenior();

  // * Solucion chatgpt 👀
  fizzBuzzChatgpt();
}
