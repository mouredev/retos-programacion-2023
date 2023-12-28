/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
#include <iostream>
#include <string>
using namespace std;

void fizzbuzz(int num){
  bool threeMultiple, fiveMultiple;
	string message;

	for (int i = 1; i <=  num; i++){
		threeMultiple = i % 3 == 0;
		fiveMultiple = i % 5 == 0;

		if (threeMultiple && fiveMultiple) {
			message = "fizzbuzz";
		}
		else if (threeMultiple) message = "fizz";
		else if (fiveMultiple) message = "buzz";
		else message = to_string(i);

		cout << message << endl;
	}
}

int main() {
  fizzbuzz(100);
}
