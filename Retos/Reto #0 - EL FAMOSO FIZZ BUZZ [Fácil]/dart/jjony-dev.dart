main() {
  for (var i = 1; i <= 100; i++) {
    String output = '';
    output += i % 3 == 0 ? 'fizz' : '';
    output += i % 5 == 0 ? 'buzz' : '';
    output += output == '' ? i.toString() : '';
    print(output);
  }
}
