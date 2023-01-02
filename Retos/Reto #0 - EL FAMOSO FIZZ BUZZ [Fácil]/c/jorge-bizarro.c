#include <stdio.h>
#include <string.h>

int main() {
  for (int i = 1; i < 101; i++) {
    if (i % 15 == 0) {
      printf("%s\n", "FizzBuzz");
    } else if (i % 5 == 0) {
      printf("%s\n", "Buzz");
    } else if (i % 3 == 0) {
      printf("%s\n", "Fizz");
    } else {
      printf("%d\n", i);
    }
  }

  return 0;
}
