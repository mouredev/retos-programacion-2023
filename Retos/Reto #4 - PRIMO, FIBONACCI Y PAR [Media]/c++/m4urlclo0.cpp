/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

#include <iostream>
#include <math.h>
using namespace std;

// Funciones 
int isPerfectSquare(int number);
string isPrime_isEven(int number);

int _number = 0;

int main() {
	cout << _number << isPrime_isEven(1) << endl;
	cout << _number << isPrime_isEven(4) << endl;
	cout << _number << isPrime_isEven(7) << endl;
	return 0;
}

int isPerfectSquare(int number) {
	int _sqrt = sqrt(number);
	return (_sqrt * _sqrt) == number;
}

string isPrime_isEven(int number) {
	string result = "";
	_number = number;
	// Verificar si el numero es par o impar
	if (number % 2 == 0) {
		result += " es par";
	}
	else {
		result += " no es par";
	}

	// verificar si el numero es primo o no
	if (number > 1) {
		for (int i = 2; i < number; i++) {
			if (number % i == 0) {
				result += ", no es primo,";
				break;
			}
			else {
				result += ", es primo,";
				break;
			}
		}
	} else {
		result += " no es primo,";
	}

	// Verificar si el numero es fibonacci
	if (isPerfectSquare(5 * number * number + 4)) {
		result += " y es fibonacci ";
	} else if (isPerfectSquare(5 * number * number - 4)) {
		result += " y es fibonacci ";
	}
	else {
		result += " y no es fibonacci ";
	}

	return result;
}