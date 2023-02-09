#include <cmath>
#include <string>
#include <iostream>

bool isPerfectSquare(int number) {
    auto result = std::sqrt(number);
    return (result * result == number);
}

/**
 * Check if the number is a fibonacci number. A number belongs to fibonacci numbers if
 * (5 * number^2 + 4) or (5 * number^2 - 4) is a perfect square.
 *
 * @param number number to check.
 * @return true if the number is fibonacci, false otherwise.
 */
bool checkFibonacci(int number) {
    return isPerfectSquare(5 * number * number + 4) || isPerfectSquare(5 * number * number - 4);
}

/**
 * Check if the number is prime. A primer number can be only divisible by one and itself.
 *
 * @param number number to check.
 * @return true if the number is prime, false otherwise.
 */
bool checkPrime(int number) {
    bool isPrime = true;
    for (int i = 2; i < number; ++i) {
        if (number % i == 0) {
            isPrime = false;
            break;
        }
    }
    return isPrime;
}

void checkNumber(int number) {
    bool isPrime = checkPrime(number);
    bool isFibonacci = checkFibonacci(number);
    auto isEven = (number % 2 == 0);

    std::string text = std::to_string(number);
    text += isPrime ? " es primo," : " no es primo,";
    text += isFibonacci ? " fibonacci" : " no es fibonacci";
    text += isEven ? " y es par." : " y es impar.";

    std::cout << text << std::endl;
}

int main(int argc, char *argv[]) {
    checkNumber(7);
}
