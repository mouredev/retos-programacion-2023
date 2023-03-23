#include <iostream>
using namespace std;

int main() {
	/*
	 * Escribe un programa que muestre por consola (con un print) los
	 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
	 * cada impresión), sustituyendo los siguientes:
	 * - Múltiplos de 3 por la palabra "fizz".
	 * - Múltiplos de 5 por la palabra "buzz".
	 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
	 */

	for (short i = 0; i < 100; i++){
		if (i % 3 == 0 && i % 5 == 0) {
			cout << "fizzbuzz\n";
		}
		else if(i % 3 == 0) {
			cout << "fizz\n";

		}
		else if(i % 5 == 0) {
			cout << "buzz\n";
		
		}
		else {
			cout << i << endl;
		}

	}

	return 0;
}