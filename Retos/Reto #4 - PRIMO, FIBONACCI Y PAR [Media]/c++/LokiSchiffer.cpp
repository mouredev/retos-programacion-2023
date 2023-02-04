/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

#include <iostream>
#include <string>
#include <cmath>
using namespace std;

bool isPrime(int number);
bool fibonnaci(int number);
string checkNumber(int number);



int main() {
	cout << checkNumber(37) << endl;
	cout << checkNumber(73) << endl;
	cout << checkNumber(5) << endl;
	cout << checkNumber(2) << endl;
	cout << checkNumber(8) << endl;
	cout << checkNumber(46) << endl;
	cout << checkNumber(13) << endl;
  
}

bool isPrime(int number) {
	// comprobar si el número es par y así descarlos todos con excepción del 2
	if (number < 2 || (number % 2 == 0 && number != 2)) {
		return false;
	}
	
	// Se revisa el modulo empezando en 3 y sin tener en cuenta los pares
	for (int i = 3; i <= (number / 2); i += 2) {
		if (number % i == 0) {
			return false;
		}
	}

	return true;
}

bool fibonnaci(int number) {
	// Se utliza la identidad de Binet para figurar si es de la secuencia de fibonnaci
	long binet = 5 * number * number;
	if (floorf(sqrt(binet+4)) == sqrt(binet+4)) {
		return true;
	}
	if (floorf(sqrt(binet-4)) == sqrt(binet-4)) {
		return true;
	}
	return false;
}

string checkNumber(int number) {
	// Crea el mensaje sobre las condiciones descritas
	string message = "El número " + to_string(number);
	message += isPrime(number) ? "" : " no";
	message += " es primo,";
	message += fibonnaci(number) ? "" : " no";
	message += " es fibonnaci y";
	message += number % 2 != 0 ? " es impar" : " es par";
	return message;
}