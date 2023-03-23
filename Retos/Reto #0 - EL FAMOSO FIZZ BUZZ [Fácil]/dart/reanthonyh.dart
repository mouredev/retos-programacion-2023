void main(List<String> args) {
  const int initalNumber = 0;
  const int finalNumber = 100;

  fizzBuzz(startOn: initalNumber, endsOn: finalNumber);
}

void fizzBuzz({required int startOn, required int endsOn}) {
  for (var number = startOn; number < endsOn; number++) {
    bool isMultTree = number % 3 == 0;
    bool isMultFive = number % 5 == 0;

    if (isMultTree && isMultFive) {
      print("fizzbuzz");
    } else if (isMultTree) {
      print("fizz");
    } else if (isMultFive) {
      print("buzz");
    } else {
      print(number);
    }
  }
}
