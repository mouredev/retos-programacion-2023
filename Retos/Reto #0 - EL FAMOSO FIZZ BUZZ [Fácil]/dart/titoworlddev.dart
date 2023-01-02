void main() {
  fizzbuzz();
}

void fizzbuzz() {
  for (int i = 1; i <= 100; i++) {
    (i % 5 == 0 && i % 3 == 0)
        ? print('fizzbuzz')
        : (i % 3 == 0)
            ? print('fizz')
            : (i % 5 == 0)
                ? print('buzz')
                : print(i);
  }
}
