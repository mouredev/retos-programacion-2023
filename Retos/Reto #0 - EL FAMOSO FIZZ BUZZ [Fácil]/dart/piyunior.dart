void main(List<String> args) {
  for (var i = 1; i <= 100; i++) {
    bool three = (i % 3) == 0;
    bool five = (i % 5) == 0;
    if (three && five) {
      print('fizzbuzz');
    } else if (three) {
      print('fizz');
    } else if (five) {
      print('buzz');
    } else {
      print(i);
    }
  }
}
