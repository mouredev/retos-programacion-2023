#include <iostream>
int main() {
  int n{1};
  while (n <= 100) {
    if (n % 3 == 0 && n % 5 == 0) {
      std::cout << "fizzbuzz" << std::endl;
    }
    if (n % 3 == 0) {
      std::cout << "fizz" << std::endl;
    }
    if (n % 5 == 0) {
      std::cout << "buzz" << std::endl;
    } else {
      std::cout << n << std::endl;
    }
      n++;
  }
  return 0;
}