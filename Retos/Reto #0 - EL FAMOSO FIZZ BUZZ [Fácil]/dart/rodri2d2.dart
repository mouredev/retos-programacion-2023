void main(List<String> args) {
  // // SOLUTION 1
  for (var i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      print('FizzBuzz');
    } else if (i % 5 == 0) {
      print('Buzz');
    } else if (i % 3 == 0) {
      print('Fizz');
    } else {
      print(i);
    }
  }

  // SOLUTION 2
  List.generate(100, (i) => i + 1).forEach(printFizzBuzz);
}

void printFizzBuzz(int value) {
  if (value % 3 == 0 && value % 5 == 0) {
    print('FizzBuzz');
  } else if (value % 5 == 0) {
    print('Buzz');
  } else if (value % 3 == 0) {
    print('Fizz');
  } else {
    print(value);
  }
}
